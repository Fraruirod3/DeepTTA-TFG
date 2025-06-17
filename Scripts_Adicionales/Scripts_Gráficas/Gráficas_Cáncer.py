import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress, spearmanr
from sklearn.metrics import mean_squared_error
from lifelines.utils import concordance_index  # pip install lifelines
import os
import numpy as np

# Cargar las predicciones
df = pd.read_csv('C:/Users/franc/Desktop/TFG/DeepTTC-main/predicciones/ByCancer/prediccion_1.csv') 

# Crear carpeta para guardar las gráficas 
save_dir = 'C:/Users/franc/Desktop/TFG/DeepTTC-main/graficas_predicciones/ByCancer/PRUEBAAAA'
os.makedirs(save_dir, exist_ok=True)

# Calcular límites globales a partir de todas las instancias
global_min = min(df['Label'].min(), df['Pred'].min())
global_max = max(df['Label'].max(), df['Pred'].max())

def annotate_metrics(ax, y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    slope, intercept, r_value, p_value, std_err = linregress(y_true, y_pred)
    pearson_r = r_value
    spearman_rho, _ = spearmanr(y_true, y_pred)
    ci = concordance_index(y_true, y_pred)
    text = (
        f"MSE: {mse:.4f}\n"
        f"RMSE: {rmse:.4f}\n"
        f"Pearson r: {pearson_r:.4f}\n"
        f"Spearman ρ: {spearman_rho:.4f}\n"
        f"C-Index: {ci:.4f}"
    )
    ax.text(0.05, 0.95, text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.7))

# === Gráfica general para todos los datos juntos ===
plt.figure(figsize=(8, 6))
ax = sns.scatterplot(x='Label', y='Pred', data=df, s=10, color='purple')

# Línea 1:1
ax.plot([global_min, global_max], [global_min, global_max],
        linestyle='--', color='gray', label='Línea 1:1')

# Misma escala en ambos ejes
ax.set_xlim(global_min, global_max)
ax.set_ylim(global_min, global_max)
ax.set_aspect('equal', 'box')

# Anotar métricas globales
annotate_metrics(ax, df['Label'], df['Pred'])

# Colocar leyenda de la línea 1:1 en esquina inferior derecha
ax.legend(loc='lower right')

ax.set_title('Relación Etiqueta vs Predicción - Todos los Tipos de Cáncer')
ax.set_xlabel('Etiqueta Real (Label)')
ax.set_ylabel('Predicción (Pred)')
ax.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'predicciones_todos_los_canceres.png'))
plt.show()

# === Gráficas por tipo de cáncer ===
for cancer_type in df['TCGA_DESC'].unique():
    cancer_data = df[df['TCGA_DESC'] == cancer_type]
    plt.figure(figsize=(8, 6))
    ax = sns.scatterplot(x='Label', y='Pred', data=cancer_data, s=10, color='purple')

    # Línea 1:1 con límites globales
    ax.plot([global_min, global_max], [global_min, global_max],
            linestyle='--', color='gray', label='Línea 1:1')

    # Misma escala en ambos ejes
    ax.set_xlim(global_min, global_max)
    ax.set_ylim(global_min, global_max)
    ax.set_aspect('equal', 'box')

    # Anotar métricas específicas del cáncer
    annotate_metrics(ax, cancer_data['Label'], cancer_data['Pred'])

    # Colocar leyenda de la línea 1:1 en esquina inferior derecha
    ax.legend(loc='lower right')

    ax.set_title(f'Relación Etiqueta vs Predicción - {cancer_type}')
    ax.set_xlabel('Etiqueta Real (Label)')
    ax.set_ylabel('Predicción (Pred)')
    ax.grid(True)
    plt.tight_layout()

    # Limpiar nombre de archivo
    safe_name = cancer_type.replace(" ", "_").replace("/", "_").replace(":", "_")
    plt.savefig(os.path.join(save_dir, f'prediccion_{safe_name}.png'))
    plt.show()
