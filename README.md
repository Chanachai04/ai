<h1>Python version 3.11.0</h1>
<hr>
<h1>ติดตั้ง</h1>
<ul>
  <li>pip install fastapi==0.121.2 uvicorn==0.38.0 pydantic==2.12.4</li>
  <li>pip install transformers==4.57.1 torch==2.2.1+cpu</li>
  <li>pip install numpy==1.26.4 protobuf==6.33.1 tiktoken==0.12.0 sentencepiece==0.2.1 safetensors==0.6.2</li>
  <li>pip install --upgrade torch --index-url https://download.pytorch.org/whl/cpu</li>
</ul>
<hr>
<h1>รันโค้ด</h1>
<p>uvicorn ai:app --host 0.0.0.0 --port 5000</p>
<hr>
<h1>DB ใช้ xampp</h1>
<p>สร้าง db</p>
<code>CREATE DATABASE mental_health_db
    DEFAULT CHARACTER SET = 'utf8mb4'
    DEFAULT COLLATE = 'utf8mb4_general_ci';</code><br><br>
<code>USE mental_health_db;</code><br><br>
<code>CREATE TABLE IF NOT EXISTS mental_health (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
    caption TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
    platform VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
    baseurl VARCHAR(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY unique_baseurl (baseurl)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;</code>

