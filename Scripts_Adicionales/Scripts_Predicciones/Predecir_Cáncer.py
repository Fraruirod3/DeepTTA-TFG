modeldir = 'C:/Users/franc/Desktop/TFG/DeepTTC-main/Registro_Modelos/Modelo_1' # Ruta del modelo
modelfile = modeldir + '/Modelo_1.pt' # Ruta del archivo del modelo

from Step2_DataEncoding import DataEncoding
from Step3_model import DeepTTC  


# Preparar datos (igual que durante el entrenamiento)
vocab_dir = 'C:/Users/franc/Desktop/TFG/DeepTTC-main'
obj = DataEncoding(vocab_dir=vocab_dir)
traindata, testdata = obj.Getdata.ByCancerEquilibrado(random_seed=1) # Cargar datos de expresión génica
traindata, train_rnadata, testdata, test_rnadata = obj.encode(
    traindata=traindata,
    testdata=testdata)

# Cargar modelo y predecir
net = DeepTTC(modeldir=modeldir)
net.load_pretrained(modelfile)

# Realizar predicciones
y_label, y_pred, mse, rmse, person, p_val, spearman, s_p_val, CI = \
    net.predict(drug_data=testdata, rna_data=test_rnadata)

print(f"Resultados:\nMSE: {mse:.4f}, RMSE: {rmse:.4f}, Pearson: {person:.4f}, Spearman: {spearman:.4f}, CI: {CI:.4f}")


# Guardar predicciones junto con la info de droga, célula y tipo de cáncer
resultados = testdata[['DRUG_ID', 'COSMIC_ID', 'TCGA_DESC']].copy()
resultados['Label'] = y_label
resultados['Pred'] = y_pred

# Ruta donde se guarda el CSV
import os
output_dir = 'C:/Users/franc/Desktop/TFG/DeepTTC-main/predicciones'
os.makedirs(output_dir, exist_ok=True)
resultados.to_csv(os.path.join(output_dir, 'prediccion_1.csv'), index=False)