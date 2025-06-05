const loginForm = document.getElementById("loginForm");
const signupForm = document.getElementById("signupForm");
const goToSignUp = document.getElementById("go-to-signup");
const goToSignIn = document.getElementById("go-to-signin");

// handle login and signup forms
signupForm.classList.add("d-none");
goToSignUp.addEventListener("click", () => {
  loginForm.classList.add("d-none");
  signupForm.classList.remove("d-none");
});

goToSignIn.addEventListener("click", () => {
  signupForm.classList.add("d-none");
  loginForm.classList.remove("d-none");
});

loginForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const formDataIn = new FormData(loginForm);

  const name = formDataIn.get("name");
  const password = formDataIn.get("password");
  console.log({ name, password });

  fetch("http://localhost:8000/api/v1/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name,
      password,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        return alert(`HTTP error status : ${response.status}`);
      }
      loginForm.reset();
      return response.json();
    })
    .then((data) => {
      location.replace("dashboard.html");
    })
    .catch((err) => console.error(err));
});

signupForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(signupForm);

  const name = formData.get("name");
  const password = formData.get("password");
  console.log({ name, password });

  fetch("http://localhost:8000/api/v1/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name,
      password,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        return alert(`HTTP error status : ${response.status}`);
      }
      loginForm.reset();
      return response.json();
    })
    .then((data) => {
      console.log(data);
    })
    .catch((err) => console.error(err));
});

const currentLocation = location.href;
if (currentLocation.includes("index.html")) {
  console.log("login url appear");
} else {
  console.log("login not appear");
}
