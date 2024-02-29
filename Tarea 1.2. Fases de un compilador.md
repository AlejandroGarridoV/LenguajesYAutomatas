# Mapa Conceptual: Fases de un Compilador

## Fases del Compilador

- **Análisis**
  - **Análisis Léxico**
  - **Análisis Sintáctico**
  - **Análisis Semántico**

- **Optimización**
  - **Optimización del Código Intermedio**
  - **Optimización del Código**

- **Generación de Código**
  - **Generación del Código Intermedio**
  - **Generación del Código Objeto**

## Herramientas del Compilador

- **Lexer**
- **Parser**
- **Semantic Analyzer**
- **Code Optimizer**
- **Code Generator**

## Ejemplo de Flujo de Trabajo

- **Análisis Léxico** → **Análisis Sintáctico** → **Análisis Semántico** → **Optimización del Código Intermedio** → **Generación del Código Objeto**

- # Fases de un Compilador

## Mapa Conceptual

```mermaid
graph TD
    A[Compilador] -->|Análisis Léxico| B(Análisis)
    A -->|Optimización de Código| C(Generación de Código)
    B -->|Análisis Sintáctico| D(Generación de Código Intermedio)
    B -->|Análisis Semántico| E(Optimización)
    C -->|Generación del Código Objeto| F(Compilación Final)

    

