# DeepTTA - Adaptación y evaluación para reposicionamiento farmacológico

Este repositorio contiene el código y configuraciones utilizadas en el Trabajo de Fin de Grado:

**" Avances en Inteligencia Artificial en elcontexto del reposicionamiento de fármacos"**

El objetivo ha sido reproducir, analizar y evaluar el modelo DeepTTA (#https://github.com/jianglikun/DeepTTC?tab=readme-ov-file), un sistema híbrido basado en Transformers y codificaciones químicas (ESPF), aplicado a la predicción de la sensibilidad celular a compuestos antitumorales.

---

## 🔍 Resumen del proyecto

- **Modelo estudiado:** DeepTTA (Transformer + MLP + codificación ESPF)
- **Datos utilizados:** Perfiles de expresión génica y estructuras moleculares (SMILES) del consorcio GDSC
- **Aportaciones principales:**
  - ✅ Reproducción funcional del modelo original en entorno local.
  - ⚖️ Diseño de particiones de datos balanceadas (`ByCancerEquilibrado`, `ByDrugEquilibrado`).
  - 📈 Visualización de resultados por tipo de cáncer y por fármaco.

---

## 📎 Notas
Este proyecto es una adaptación académica del modelo original DeepTTC.
La implementación se ha reestructurado para facilitar la comprensión, experimentación y evaluación del modelo en un entorno reproducible.

Francisco Javier Ruiz Rodríguez
Grado en Ingeniería de la Salud – mención en Informática Clínica
Universidad de Sevilla, 2025
