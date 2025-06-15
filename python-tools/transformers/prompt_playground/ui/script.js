const promptForm = document.getElementById("prompt-form");
const resultField = document.getElementById("result");
const resultClearBtn = document.getElementById("result-btn");

resultClearBtn.addEventListener("click", () => {
  resultField.innerText = "";
  resultField.classList.add("d-none");
  resultClearBtn.classList.add("d-none");
});

promptForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(promptForm);
  const prompt = formData.get("prompt");
  const temperature = formData.get("temp");
  const topK = formData.get("top-k");
  const topP = formData.get("top-p");
  const maxNewTokns = formData.get("max-new-tokens");

  const data = {
    prompt: prompt,
    temperature: parseFloat(temperature),
    top_k: parseInt(topK),
    top_p: parseFloat(topP),
    max_new_tokens: parseInt(maxNewTokns),
  };

  resultField.classList.remove("d-none");
  resultField.innerText = "generating...";
  fetch("http://localhost:8000/api/v1/generate", {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      const reader = response.body.getReader();
      const decoder = new TextDecoder("utf-8");
      resultField.innerText = "";

      function read() {
        reader.read().then(({ done, value }) => {
          if (done) {
            resultField.innerText += "\n ----end----";
            return;
          }

          const chunk = decoder.decode(value, { stream: true });
          resultField.innerText += chunk;
          resultField.innerHTML += "&nbsp";
          read();
        });
      }
      read();
    })
    .catch((err) => {
      console.error(err);
    });
});
