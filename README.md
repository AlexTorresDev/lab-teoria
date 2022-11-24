## Leer

En la carpeta New se encuentra lo nuevo, el código es muy sencillo de usar solo se importa Qam y se le pasan parámetros.

Ejemplo:

```python
import numpy as np
from new_qam import NewQam

data = np.array([1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0])
qam = NewQam(8, fCarrier=50, fs=12000, baud=120)
qam.generate_signal(data)
qam.plot_signal('Primera señal')
```

Las propiedades de la señal son:


| Propiedad   | Descripción                 | Valor por defecto |
| ----------- | --------------------------- | ----------------- |
| `Nbits`     | Número de bits M            | 8                 |
| `fCarrier`  | Frecuencia de la portadora  | 50                |
| `fs`        | Frecuencia de sampleo       | 12000             |
| `baud`      | tasa de baudios             | 120               |