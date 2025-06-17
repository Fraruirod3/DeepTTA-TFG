import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress, spearmanr
from sklearn.metrics import mean_squared_error
from lifelines.utils import concordance_index  # pip install lifelines
import os
import numpy as np

# Cargar los datos
df = pd.read_csv('C:/Users/franc/Desktop/TFG/DeepTTC-main/predicciones/ByDrug/predicciones_bydrug.csv')

# Crear carpeta para guardar las gráficas
save_dir = 'C:/Users/franc/Desktop/TFG/DeepTTC-main/graficas_predicciones/ByDrug/Modelo_4b'
os.makedirs(save_dir, exist_ok=True)

# Calcular límites globales
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

# === Gráfica general para todos los fármacos juntos ===
plt.figure(figsize=(8, 6))
ax = sns.scatterplot(x='Label', y='Pred', data=df, s=10, color='purple')

# Línea 1:1
ax.plot([global_min, global_max], [global_min, global_max],
        linestyle='--', color='gray', label='Línea 1:1')

# Misma escala
ax.set_xlim(global_min, global_max)
ax.set_ylim(global_min, global_max)
ax.set_aspect('equal', 'box')

# Anotar métricas
annotate_metrics(ax, df['Label'], df['Pred'])

ax.set_title('Relación Etiqueta vs Predicción - Todos los Fármacos')
ax.set_xlabel('Etiqueta Real (Label)')
ax.set_ylabel('Predicción (Pred)')

# Ubicar la leyenda de la línea 1:1 en esquina inferior derecha
ax.legend(loc='lower right')

ax.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'predicciones_todos_los_farmacos.png'))
plt.show()


# === Gráficas por fármaco ===
for drug in df['DRUG_ID'].unique():
    sub = df[df['DRUG_ID'] == drug]
    plt.figure(figsize=(8, 6))
    ax = sns.scatterplot(x='Label', y='Pred', data=sub, s=10, color='purple')

    # Línea 1:1
    ax.plot([global_min, global_max], [global_min, global_max],
            linestyle='--', color='gray', label='Línea 1:1')

    # Misma escala
    ax.set_xlim(global_min, global_max)
    ax.set_ylim(global_min, global_max)
    ax.set_aspect('equal', 'box')

    # Métricas
    annotate_metrics(ax, sub['Label'], sub['Pred'])

    ax.set_title(f'Relación Etiqueta vs Predicción - {drug}')
    ax.set_xlabel('Etiqueta Real (Label)')
    ax.set_ylabel('Predicción (Pred)')

    # Ubicar la leyenda de la línea 1:1 en esquina inferior derecha
    ax.legend(loc='lower right')

    ax.grid(True)
    plt.tight_layout()

    safe_name = str(drug).replace(" ", "_").replace("/", "_").replace(":", "_")
    plt.savefig(os.path.join(save_dir, f'prediccion_{safe_name}.png'))
    plt.show()
