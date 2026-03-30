import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
# Настраваем количество колонок и строк
cols, rows = 8, 8

# Генерируем названия строк и столбцов
col_names = [f"Column_{i+1}" for i in range(cols)]
row_names = [f"Row_{i+1}" for i in range(rows)]

# Функция для генерации рандомных чисел в матрице
def random_matrix_generator(save_file_path):
    random_matrix = np.random.randint(10, 100, size=(rows, cols))
    print(random_matrix)
    # Добавляем все данные в DataFrame для экспорта в Excel
    df_original = pd.DataFrame(random_matrix, columns=col_names, index=row_names)
    # Создаем таблицу с данными
    df_original.to_excel(save_file_path, sheet_name='Sheet', index=True)

# Генерируем рандомные числа
random_matrix_generator('./data.xlsx')

# Загружаем таблицу
df_loaded = pd.read_excel('./data.xlsx', sheet_name='Sheet', index_col=0)

matrix = df_loaded.to_numpy()

arrays = {col: df_loaded[col].to_numpy() for col in df_loaded.columns}

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Matrix - view', fontsize=16, fontweight='bold')

# Тепловая карта
ax1 = axes[0]
im = ax1.imshow(matrix, cmap="YlOrRd", aspect="auto")
ax1.set_title("Тепловая карта", fontsize=12, fontweight="bold")
ax1.set_xticks(range(cols))
ax1.set_xticklabels([f"С{i + 1}" for i in range(cols)])
ax1.set_yticks(range(rows))
ax1.set_yticklabels([f"С{i + 1}" for i in range(rows)])

# Подписи значений внутри ячеек
for i in range(rows):
    for j in range(cols):
        val = matrix[i, j]
        color = "white" if val > 70 else "black"
        ax1.text(j, i, str(val), ha="center", va="center",
                 fontsize=9, color=color, fontweight="bold")

plt.colorbar(im, ax=ax1, shrink=0.8)

# График
ax2 = axes[1]
colors = plt.cm.tab10(np.linspace(0, 1, cols))
x = np.arange(1, rows + 1)

for idx, col in enumerate(df_loaded.columns):
    ax2.plot(x, arrays[col], marker="o", label=col, color=colors[idx], linewidth=1.8, markersize=5)

ax2.set_title('Matrix', fontsize=16, fontweight='bold', y=1.02)
ax2.set_xlabel('row')
ax2.set_ylabel('value')
ax2.set_xticks(x)
ax2.legend(fontsize=8, ncol=2)
ax2.grid(True, linestyle='--', alpha=0.5)

# Столбцы
ax3 = axes[2]
means = matrix.mean(axis=0)
stds = matrix.std(axis=0)
bar_colors = plt.cm.viridis(np.linspace(0.2, 0.85, cols))

bars = ax3.bar(col_names, means, yerr=stds, capsize=5,
               color=bar_colors, edgecolor="gray", linewidth=0.7)

ax3.set_title("Среднее ± стд. откл. по столбцам", fontsize=12, fontweight="bold")
ax3.set_xlabel("Столбец")
ax3.set_ylabel("Среднее значение")
ax3.tick_params(axis="x", rotation=30)

for bar, m in zip(bars, means):
    ax3.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 1.5, f"{m:.1f}",
             ha="center", va="bottom", fontsize=9, fontweight="bold")

ax3.grid(True, axis="y", linestyle="--", alpha=0.4)

# Показать интерфейс
# plt.show()

# Созранение картинки
plt.tight_layout()
plt.savefig('./matrix.png', dpi=150, bbox_inches='tight')

plt.close()
