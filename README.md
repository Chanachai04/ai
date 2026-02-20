<h1>Python version 3.11.0</h1>
<hr>
<h1>ติดตั้ง</h1>

```powershall
  # 1. ลง PyTorch CPU ให้เสร็จก่อน (ใช้เวอร์ชันใหม่กว่า 2.2.1 เพื่อรองรับ Transformers 4.57)
  pip install "torch==2.6.0+cpu" --extra-index-url https://download.pytorch.org/whl/cpu

  # 2. ลง Library อื่นๆ (ไม่ต้องลง torch ซ้ำแล้ว)
  pip install fastapi==0.121.2 uvicorn==0.38.0 pydantic==2.12.4
  pip install transformers==4.57.1
  pip install numpy==1.26.4 protobuf==6.33.1 tiktoken==0.12.0 sentencepiece==0.2.1 safetensors==0.6.2

  pip install fastapi uvicorn pydantic transformers torch sentencepiece protobuf tiktoken
```

<hr>
<h1>รันโค้ด</h1>

```powershall
uvicorn ai:app --host 0.0.0.0 --port 5000
```
<hr>
<h1>DB ใช้ xampp</h1>
<p>สร้าง db</p>

```
CREATE DATABASE mental_health_db
    DEFAULT CHARACTER SET = 'utf8mb4'
    DEFAULT COLLATE = 'utf8mb4_general_ci';
```

```
USE mental_health_db;
```

```
CREATE TABLE IF NOT EXISTS mental_health (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
    caption TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
    platform VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
    baseurl VARCHAR(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY unique_baseurl (baseurl)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```

