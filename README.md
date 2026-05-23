# Sistema de Inventario Visual y Auditoría de Seguridad para Telecomunicaciones

**Proyecto Final - Seguridad de la Información**
**Estudiante:** David
**Programa:** Ingeniería en Telecomunicaciones
**Institución:** Fundación Universitaria Compensar
**Fecha:** 22 de Mayo de 2026

---

## Tabla de Contenido
- [Introducción](#introducción)
- [Objetivo General](#objetivo-general)
- [Módulos del Proyecto](#módulos-del-proyecto)
- [Simulación Completa](#simulación-completa)
- [Matriz de Riesgos](#matriz-de-riesgos)
- [Declaración de Aplicabilidad (SoA)](#declaración-de-aplicabilidad-soa)
- [Conclusiones](#conclusiones)

---

## Introducción
Este proyecto desarrolla un **sistema automatizado** que permite realizar inventarios visuales de activos de red mediante **YOLOv8**, proteger la información con criptografía y auditar el cumplimiento de la **ISO 27001:2022**.

---

## Objetivo General
Desarrollar un sistema que detecte activos de telecomunicaciones mediante YOLO, asegure su transmisión cifrada y evalúe el cumplimiento de la norma ISO 27001.

---

## Módulos del Proyecto

### Módulo 1 - Detección con YOLOv8
- Detección de: Router, Switch, Firewall, Servidor, Access Point.
- Tecnologías: YOLOv8 + Roboflow.

### Módulo 2 - Cifrado de la Información
- Hashing (SHA-256)
- Cifrado Híbrido (RSA + AES-256)

### Módulo 3 - Auditoría ISO 27001
Evaluación de controles clave de la norma.

---

## Simulación Completa
**Resultado de la simulación:**
- 4 equipos detectados correctamente (Switch, Router, Firewall, Servidor).
- Información cifrada exitosamente.
- Reporte de auditoría generado.

---

## Matriz de Riesgos

| Riesgo | Probabilidad | Impacto | Nivel | Mitigación |
|-------------------------------|--------------|---------|---------|-----------------------------|
| Interceptación de datos | Media | Alto | Alto | Cifrado híbrido RSA+AES |
| Falsa detección YOLO | Baja | Medio | Medio | Umbral de confianza > 0.75 |
| Robo del dispositivo | Alta | Alto | Crítico | Encriptación del móvil |
| Pérdida de integridad | Baja | Alto | Alto | Hash SHA-256 |

---

## Declaración de Aplicabilidad (SoA)

| Control ISO 27001 | Estado | Justificación |
|-------------------------|----------|-------------|
| A.5.9 Inventario | Cumple | Detección automática YOLO |
| A.8.24 Criptografía | Cumple | AES + RSA + Hashing |
| A.5.10 Uso aceptable | Cumple | Uso exclusivo para inventario |

---

## Conclusiones
El sistema cumple con todos los requisitos del proyecto. Solución práctica, segura y alineada con las necesidades de un ingeniero en telecomunicaciones.

