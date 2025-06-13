const promptForm = document.getElementById("prompt-form");

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

  fetch("http://localhost:8000/api/v1/generate", {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log(data.result);
    })
    .catch((err) => {
      console.error(err);
    });

  // promptForm.reset();
});
