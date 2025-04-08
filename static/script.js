document.getElementById("callApiBtn").addEventListener("click", async () => {
    try {
      const response = await fetch("/api/hello");
      const data = await response.json();
      document.getElementById("apiResponse").innerText = data.message;
    } catch (error) {
      document.getElementById("apiResponse").innerText = "Error calling API";
    }
  });
  
