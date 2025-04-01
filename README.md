# Flask Energy Predictor Add-on for Home Assistant

Este es un add-on personalizado para Home Assistant que ejecuta un backend en Flask con un modelo **ARIMA** para predecir el consumo energético futuro basado en datos históricos.

## 🚀 ¿Qué hace?

Este microservicio expone una API REST en el puerto `5000` que acepta datos de consumo energético (por mes) y devuelve predicciones para los próximos **1, 2 y 3 meses** usando un modelo ARIMA.

## 📦 Instalación

1. Clona este repositorio en tu máquina o súbelo directamente a GitHub.
2. En Home Assistant, ve a:
   - `Ajustes > Add-ons > Tienda de complementos`
   - Haz clic en `⋮` y selecciona `Repositorios`
   - Añade tu repositorio de GitHub como URL personalizada:

     ```
     https://github.com/rafajaramillo/hassio-addons
     ```

3. Pulsa **Agregar** y verás el add-on `Flask Energy Predictor`.
4. Instálalo y ejecútalo.

## 🔌 Endpoint

- **POST** `/predecir`
- **Content-Type:** `application/json`
- **Body:**

```json
{
  "fechas": ["2024-01", "2024-02", "2024-03"],
  "consumos": [120.5, 130.2, 128.0]
}
```

- **Respuesta:**

```json
{
  "predicciones_kwh": {
    "proximo_mes": 132.4,
    "dos_meses": 135.1,
    "tres_meses": 137.8
  }
}
```

## 🧠 ¿Cómo se conecta con Flutter?

Puedes hacer una solicitud HTTP desde Flutter a:

```
http://<IP_HOME_ASSISTANT>:5000/predecir
```

---

## 📁 Estructura del add-on

```
flask_energia/
├── Dockerfile
├── config.json
├── app.py
├── run.sh
└── requirements.txt
```

---

## 🧑‍💻 Autor

Desarrollado por [rafajaramillo](https://github.com/rafajaramillo)