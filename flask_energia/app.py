from flask import Flask, request, jsonify
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

app = Flask(__name__)

@app.route('/predecir', methods=['POST'])
def predecir_consumo():
    try:
        data = request.get_json()
        fechas = data.get('fechas')
        consumos = data.get('consumos')

        if not fechas or not consumos or len(fechas) != len(consumos):
            return jsonify({'error': 'Datos inválidos'}), 400

        df = pd.DataFrame({'fecha': pd.to_datetime(fechas), 'consumo': consumos})
        df.set_index('fecha', inplace=True)

        modelo = ARIMA(df['consumo'], order=(1, 1, 1))
        modelo_entrenado = modelo.fit()
        pred = modelo_entrenado.forecast(steps=3)
        pred_list = [round(val, 2) for val in pred]

        return jsonify({
            'predicciones_kwh': {
                'proximo_mes': pred_list[0],
                'dos_meses': pred_list[1],
                'tres_meses': pred_list[2]
            }
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
