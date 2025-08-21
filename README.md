# Mi API FastAPI - Semana 2

## ¿Qué hace?

API mejorada con validación automática de datos y type hints.

## Nuevos Features (Semana 2)

- ✅ Type hints en todas las funciones
- ✅ Validación automática con Pydantic
- ✅ Endpoint POST para crear datos
- ✅ Parámetros de ruta (ejemplo: /products/{id})
- ✅ Búsqueda con parámetros query

## ¿Cómo ejecutar?

```bash
pip install fastapi pydantic uvicorn
uvicorn main:app --reload
```


## REFLEXION:

# ¿Los type hints hacen tu código más claro? ¿Por qué?:

Porque ante posibles errores, quizas el error sea por el tipo de informacion que llega esperando otro, aun asi es mas facil leerlo y legible al entender que llega y que podria ocasionar errores apoyando al mantenimiento y limpieza del codigo

# ¿Cómo te ayuda Pydantic a crear APIs más robustas?

Pydantic aporta robustez al verificar la llegada de datos, sencillamente aportando ese control a los datos que llegan y cortando la llegada de estos en caso de no ser el tipo de dato que se esperaria que llegara.

# ¿Cómo mejoraron estos conceptos tu API comparada con Semana 1?

La api es un sistema complejo y confuso para los que son nuevos y se ingegran nuevos en este mundo, por lo tanto ir avanzando lentamente resulta gratificante teniendo en cuenta que estos conocimientos podrian llegar a servir para el desarrollo y posterior depuracion de mi proyecto.