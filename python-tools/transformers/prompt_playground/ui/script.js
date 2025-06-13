const promptForm = document.getElementById("prompt-form");

promptForm.addEventListener("submit", (event) => {
  event.preventDefault();
  console.log("its coming");

  const formData = new FormData(promptForm);
  const prompt = formData.get("prompt");
  const temperature = formData.get("temp");
  const topK = formData.get("top-k");
  const topP = formData.get("top-p");

  console.log(prompt, temperature, topK, topP);
});
