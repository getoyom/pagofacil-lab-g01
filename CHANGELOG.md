# Changelog

Todos los cambios notables de este proyecto se documentan aquí.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y
[Versionado Semántico](https://semver.org/lang/es/).

## [Sin publicar]

## [1.0.0]
### Agregado
- Cálculo de la comisión de transferencias (`calcular_comision`).
- Cálculo del total a debitar (`calcular_total`).
- Validación del monto (`validar_monto`).

## [1.0.1] - 2026 - 10 - 05
### Corregido 
 - Correción de validación en `calcular_comision`: Si el monto es 100, no tiene comisión
 - Correción de comisión maxima en `calcular_comision`: Validar si una comisión es mayor a 25, en caso así sea, dejarla en 25
 - Correción en `calcular_total`: Cambio de signo para calcular total
