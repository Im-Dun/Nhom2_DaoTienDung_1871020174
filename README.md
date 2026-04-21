# 🧭 Maze Solver Visualization (BFS & DFS)

Dự án mô phỏng và trực quan hóa quá trình tìm đường trong mê cung sử dụng hai thuật toán:

* Breadth-First Search (BFS)
* Depth-First Search (DFS)

Ứng dụng hiển thị trực tiếp quá trình duyệt và đường đi tìm được bằng thư viện **Pygame**.

---

## 🎯 Mục tiêu

* Hiểu rõ cách hoạt động của BFS và DFS
* So sánh hiệu quả giữa hai thuật toán
* Trực quan hóa quá trình tìm đường trong mê cung

---

## ⚙️ Công nghệ sử dụng

* Python 3
* Pygame (visualization)
* Cấu trúc dữ liệu: Queue (BFS), Stack (DFS), Set

---

## 📂 Cấu trúc project

```
project-root/
│
├── maps/
│   ├── maze_basic.py      # Mê cung 5x5
│   ├── maze_hard.py       # Mê cung 10x10
│
├── src/
│   ├── bfs_solver.py      # Thuật toán BFS
│   ├── dfs_solver.py      # Thuật toán DFS
│   ├── core_logic.py      # Logic chung (neighbors, start/goal)
│
├── main.py                # Chạy chương trình + visualize
└── README.md
```

---

## 🧠 Thuật toán

### 🔵 BFS (Breadth-First Search)

* Sử dụng hàng đợi (queue)
* Luôn tìm được đường đi ngắn nhất
* Duyệt theo từng lớp

→ Cài đặt tại: `bfs_solver.py` 

---

### 🟡 DFS (Depth-First Search)

* Sử dụng stack
* Không đảm bảo đường đi ngắn nhất
* Đi sâu trước rồi quay lui

→ Cài đặt tại: `dfs_solver.py` 

---

## 🧩 Logic chung

* Tìm điểm bắt đầu (S) và kết thúc (G)
* Sinh các ô lân cận hợp lệ
* In kết quả và visualize

→ Xem tại: `core_logic.py` 

---

## 🗺️ Mê cung

### Bản đồ cơ bản (5x5)

* Nhỏ, dễ quan sát
* Dùng để test nhanh

→ `maze_basic.py` 

### Bản đồ nâng cao (10x10)

* Phức tạp hơn
* Dùng để so sánh hiệu năng

→ `maze_hard.py` 

---

## ▶️ Cách chạy chương trình

### 1. Clone repo

```bash
git clone <repo-url>
cd <project-folder>
```

### 2. Cài thư viện

```bash
pip install pygame
```

### 3. Chạy

```bash
python main.py
```

---

## 🎮 Visualization

* 🟩 Start (S)
* 🟥 Goal (G)
* ⬛ Tường
* 🟨 Ô đã duyệt
* 🔵 Đường đi tìm được

Pygame sẽ mở cửa sổ hiển thị trực tiếp kết quả.

---

## 📊 So sánh BFS vs DFS

| Tiêu chí        | BFS        | DFS              |
| --------------- | ---------- | ---------------- |
| Đường ngắn nhất | ✔          | ✖                |
| Tốc độ          | Trung bình | Nhanh (tùy case) |
| Bộ nhớ          | Cao        | Thấp             |
| Chiến lược      | Rộng       | Sâu              |

---

## 📌 Ghi chú

* Thứ tự duyệt neighbor ảnh hưởng kết quả DFS
* BFS luôn ổn định hơn khi cần shortest path
* DFS phù hợp khi cần tìm nhanh 1 lời giải bất kỳ

---

## 📄 License

Dự án phục vụ mục đích học tập
