# Framework de Pruebas Automatizadas con Selenium

Este repositorio contiene pruebas automatizadas utilizando el framework Selenium para realizar pruebas de extremo a extremo en la aplicación "Biblioteca-Apiux". Estas pruebas están diseñadas para verificar la funcionalidad del proceso de inicio de sesión y otras características relacionadas con la autenticación.

## Descripción

Este proyecto está enfocado en la automatización de pruebas de software utilizando Selenium, un conjunto de herramientas para la automatización de navegadores web. El objetivo principal es garantizar que el proceso de inicio de sesión en la aplicación "Biblioteca-Apiux" funcione correctamente y que se manejen adecuadamente diferentes escenarios, como credenciales válidas e inválidas, campos vacíos y más.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `src/functions/functions.py`: Este archivo contiene funciones de utilidad y métodos que se utilizan en las pruebas automatizadas.

- `/test/`: Estos archivos contienen las pruebas automatizadas utilizando el framework Selenium. Se dividen en varios métodos que prueban diferentes aspectos del proceso de inicio a fin de la aplicación.

- `report/`: (Privada) Esta carpeta se utiliza para almacenar los informes generados después de la ejecución de las pruebas. Los informes están en formato HTML y proporcionan una visión detallada de los resultados de las pruebas.

El resultado de las pruebas se generará en la carpeta report en formato HTML para su posterior revisión.

## Integración con Jenkins
Este proyecto se integra fácilmente con Jenkins para la ejecución continua de pruebas. Cuando se ejecuta en Jenkins, genera un informe de prueba actualizado automáticamente en formato HTML y proporciona información detallada sobre el estado de las pruebas.

## Informe de Pruebas
Después de ejecutar las pruebas, puede acceder al informe de pruebas generado en la carpeta report. Este informe incluye información sobre las pruebas realizadas, sus resultados, capturas de pantalla y mensajes de error, lo que facilita la identificación y resolución de problemas.
