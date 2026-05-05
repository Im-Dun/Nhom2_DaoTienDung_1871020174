# 🧭 Maze Solver Visualization (BFS & DFS)

**Sinh viên:** Đào Tiến Dũng – MSSV: 1871020174 – Nhóm 2

Dự án mô phỏng và trực quan hóa quá trình tìm đường trong mê cung sử dụng hai thuật toán:

* **Breadth-First Search (BFS)** – Tìm kiếm theo chiều rộng
* **Depth-First Search (DFS)** – Tìm kiếm theo chiều sâu

Ứng dụng hiển thị trực tiếp quá trình duyệt và đường đi tìm được bằng thư viện **Pygame**.

---

## 🎯 Mục tiêu

* Hiểu rõ cách hoạt động của BFS và DFS
* So sánh hiệu quả giữa hai thuật toán trên hai bản đồ khác nhau
* Trực quan hóa quá trình tìm đường trong mê cung bằng Pygame

---

## ⚙️ Công nghệ sử dụng

* Python 3
* Pygame (trực quan hóa)
* Cấu trúc dữ liệu: Queue / deque (BFS), Stack / list (DFS), Set (visited)

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
│   ├── core_logic.py      # Logic chung (neighbors, start/goal, in kết quả)
│   ├── main.py            # Chạy chương trình + visualize Pygame
│
└── README.md
```

---

## 🧠 Thuật toán

### 🔵 BFS (Breadth-First Search)

* Sử dụng hàng đợi (`deque`)
* Duyệt theo từng lớp (theo chiều rộng)
* **Luôn tìm được đường đi ngắn nhất**

→ Cài đặt tại: `src/bfs_solver.py`

### 🟡 DFS (Depth-First Search)

* Sử dụng ngăn xếp (`list`)
* Đi sâu trước, quay lui khi bế tắc
* **Không đảm bảo đường đi ngắn nhất**

→ Cài đặt tại: `src/dfs_solver.py`

### 🧩 Logic chung (`core_logic.py`)

* `get_start_goal(maze)` – Tìm vị trí điểm bắt đầu (S) và kết thúc (G)
* `get_neighbors(maze, node)` – Sinh các ô lân cận hợp lệ (thứ tự: Phải → Xuống → Lên → Trái)
* `print_maze_with_path(maze, path, visited_count)` – In mê cung với đường đi ra console

---

## 🗺️ Mê cung

### Bản đồ cơ bản (5x5) – `maps/maze_basic.py`

```
 S  .  █  .  .
 .  .  █  .  .
 .  .  .  .  G
 █  █  .  █  █
 .  .  .  .  .
```

* `S` = Điểm bắt đầu `(0,0)`, `G` = Đích `(2,4)`
* `█` = Tường, `.` = Đường đi

### Bản đồ khó (10x10) – `maps/maze_hard.py`

```
 S  .  █  .  .  █  .  .  █  .
 .  .  █  .  █  █  .  █  █  .
 .  █  .  .  █  .  .  █  .  .
 .  █  █  █  █  .  █  █  .  █
 .  .  .  .  .  .  .  █  .  █
 █  █  █  █  █  █  .  █  .  █
 .  .  .  .  .  .  .  .  .  .
 .  █  █  █  █  █  █  █  █  .
 .  .  .  .  .  .  .  .  .  .
 █  █  █  █  █  █  .  █  █  G
```

* `S` = Điểm bắt đầu `(0,0)`, `G` = Đích `(9,9)`

---

## 📊 Kết quả thực nghiệm

### Bản đồ cơ bản (5x5)

| Thuật toán | Đường đi tìm được | Độ dài | Số ô đã duyệt |
|---|---|---|---|
| **BFS** | (0,0)→(0,1)→(1,1)→(2,1)→(2,2)→(2,3)→(2,4) | **7 bước** | **12 ô** |
| **DFS** | (0,0)→(1,0)→(2,0)→(2,1)→(2,2)→(2,3)→(2,4) | 7 bước | 19 ô |

**Hình ảnh đường đi BFS (bản đồ cơ bản):**
```
 S  +  █  .  .
 .  +  █  .  .
 .  +  +  +  G
 █  █  .  █  █
 .  .  .  .  .
```

**Hình ảnh đường đi DFS (bản đồ cơ bản):**
```
 S  .  █  .  .
 +  .  █  .  .
 +  +  +  +  G
 █  █  .  █  █
 .  .  .  .  .
```

> Trên bản đồ 5x5, cả BFS và DFS đều tìm được đường đi dài **7 bước** (ngắn nhất).  
> Tuy nhiên, BFS chỉ duyệt **12 ô** trong khi DFS duyệt **19 ô** — BFS hiệu quả hơn.

---

### Bản đồ khó (10x10)

| Thuật toán | Độ dài đường đi | Số ô đã duyệt |
|---|---|---|
| **BFS** | **19 bước** ✅ (ngắn nhất) | **38 ô** |
| **DFS** | 31 bước ❌ (không ngắn nhất) | 51 ô |

**Chi tiết đường đi BFS (19 bước):**
```
(0,0)→(1,0)→(2,0)→(3,0)→(4,0)→(4,1)→(4,2)→(4,3)→(4,4)→(4,5)
→(4,6)→(5,6)→(6,6)→(6,7)→(6,8)→(6,9)→(7,9)→(8,9)→(9,9)
```

**Chi tiết đường đi DFS (31 bước):**
```
(0,0)→(1,0)→(2,0)→(3,0)→(4,0)→(4,1)→(4,2)→(4,3)→(4,4)→(4,5)
→(4,6)→(5,6)→(6,6)→(6,5)→(6,4)→(6,3)→(6,2)→(6,1)→(6,0)→(7,0)
→(8,0)→(8,1)→(8,2)→(8,3)→(8,4)→(8,5)→(8,6)→(8,7)→(8,8)→(8,9)→(9,9)
```

**Hình ảnh đường đi BFS (bản đồ khó):**
```
 S  .  █  .  .  █  .  .  █  .
 +  .  █  .  █  █  .  █  █  .
 +  █  .  .  █  .  .  █  .  .
 +  █  █  █  █  .  █  █  .  █
 +  +  +  +  +  +  +  █  .  █
 █  █  █  █  █  █  +  █  .  █
 .  .  .  .  .  .  +  +  +  +
 .  █  █  █  █  █  █  █  █  +
 .  .  .  .  .  .  .  .  .  +
 █  █  █  █  █  █  .  █  █  G
```

**Hình ảnh đường đi DFS (bản đồ khó):**
```
 S  .  █  .  .  █  .  .  █  .
 +  .  █  .  █  █  .  █  █  .
 +  █  .  .  █  .  .  █  .  .
 +  █  █  █  █  .  █  █  .  █
 +  +  +  +  +  +  +  █  .  █
 █  █  █  █  █  █  +  █  .  █
 +  +  +  +  +  +  +  .  .  .
 +  █  █  █  █  █  █  █  █  .
 +  +  +  +  +  +  +  +  +  +
 █  █  █  █  █  █  .  █  █  G
```

> Trên bản đồ 10x10, BFS tìm được đường đi **ngắn nhất** (19 bước) và duyệt **ít ô hơn** (38 ô).  
> DFS đi đường vòng hơn (31 bước) và duyệt nhiều ô hơn (51 ô).

---

## 📊 So sánh tổng quát BFS vs DFS

| Tiêu chí | BFS | DFS |
|---|---|---|
| Đường đi ngắn nhất | ✅ Luôn đảm bảo | ❌ Không đảm bảo |
| Số ô duyệt (5x5) | 12 ô | 19 ô |
| Số ô duyệt (10x10) | 38 ô | 51 ô |
| Độ dài đường đi (5x5) | 7 bước | 7 bước |
| Độ dài đường đi (10x10) | **19 bước** | 31 bước |
| Cấu trúc dữ liệu | Queue (deque) | Stack (list) |
| Chiến lược duyệt | Theo chiều rộng | Theo chiều sâu |
| Bộ nhớ sử dụng | Cao hơn | Thấp hơn |

---

## ▶️ Cách chạy chương trình

### 1. Clone repo

```bash
git clone https://github.com/Im-Dun/Nhom2_DaoTienDung_1871020174.git
cd Nhom2_DaoTienDung_1871020174
```

### 2. Cài thư viện

```bash
python -m pip install -U pygame==2.6.0
```

### 3. Chạy chương trình

```bash
python src/main.py
```

Chương trình sẽ chạy lần lượt 4 lượt (BFS + DFS trên từng bản đồ). Mỗi lượt mở một cửa sổ Pygame — đóng cửa sổ để tiếp tục lượt tiếp theo.

---

## 🎮 Chú thích màu sắc Visualization (Pygame)

| Màu | Ý nghĩa |
|---|---|
| 🟩 Xanh lá | Điểm bắt đầu (S) |
| 🟥 Đỏ | Đích đến (G) |
| ⬛ Đen | Tường |
| 🟨 Vàng | Ô đã được duyệt qua |
| 🔵 Xanh dương | Đường đi giải pháp |
| ⬜ Xám nhạt | Ô chưa duyệt (đường đi tự do) |

---

## 📌 Nhận xét & Kết luận

* **BFS luôn tìm được đường đi ngắn nhất** nhờ duyệt theo từng lớp đều nhau.
* **DFS không đảm bảo đường đi ngắn nhất** — kết quả phụ thuộc vào thứ tự duyệt neighbor.
* Thứ tự duyệt neighbor (Phải → Xuống → Lên → Trái) ảnh hưởng đáng kể đến đường đi DFS tìm được.
* Với bản đồ 10x10, BFS vượt trội rõ rệt: đường đi ngắn hơn 12 bước và duyệt ít hơn 13 ô so với DFS.
* **Kết luận:** Dùng BFS khi cần đường đi ngắn nhất; dùng DFS khi cần tìm nhanh bất kỳ một lời giải.

---

## 📄 License

Dự án phục vụ mục đích học tập – môn Trí Tuệ Nhân Tạo.
