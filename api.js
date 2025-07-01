// // The text you want to analyze
// const textToAnalyze =
//   "ดู “สูตรลับตำรับดันเจียน” จบแล้ว จะบอกว่าดีเกินคาดไปมากกก นี่ว่าเรื่องมันเครียดอยู่นะ แต่ตลค.สามารถทำให้เราหลุดขำได้อะ โดนเส้นเกิน  อนิเมะภาพสวยตาแตกสุดๆ อาหารน่ากินทุกอย่าง ดูเฉยๆไม่ได้ต้องตักข้าวมากินด้วย \n\nปกติไม่ค่อยได้ดูแนวนี้เท่าไหร่ แต่สำหรับเรื่องนี้ให้เลย สนุกมากจริง!!!"; // Example Thai text

// The URL of your Flask API
const apiUrl = "http://127.0.0.1:5000/sentiment"; // Replace with your actual API endpoint

// Function to call the sentiment analysis API
async function getSentimentAnalysis(text) {
  try {
    // Sending a POST request to the Flask API
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: text }), // Sending the text as a JSON payload
    });

    // Checking if the response is OK (status 200)
    if (!response.ok) {
      throw new Error("Failed to analyze sentiment");
    }

    // Parsing the JSON response
    const data = await response.json();

    // Accessing sentiment data
    const sentiment = data.sentiment;
    console.log("Sentiment Score:", sentiment.score);
    console.log("Sentiment Magnitude:", sentiment.magnitude);

    // You can display or use this data as needed
  } catch (error) {
    console.error("Error:", error);
  }
}

// Call the function with the text you want to analyze
// getSentimentAnalysis(textToAnalyze);
