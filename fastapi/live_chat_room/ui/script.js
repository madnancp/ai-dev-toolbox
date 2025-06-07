// check is user authenticated

const loginForm = document.getElementById("loginForm");
const signupForm = document.getElementById("signupForm");
const goToSignUp = document.getElementById("go-to-signup");
const goToSignIn = document.getElementById("go-to-signin");
const logoutBtn = document.getElementById("logout-btn");

// handle login and signup forms
if (loginForm && signupForm) {
  signupForm.classList.add("d-none");
  goToSignUp.addEventListener("click", () => {
    signupForm.classList.remove("d-none");
    loginForm.classList.add("d-none");
  });

  goToSignIn.addEventListener("click", () => {
    loginForm.classList.remove("d-none");
    signupForm.classList.add("d-none");
  });

  loginForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const formDataIn = new FormData(loginForm);

    const name = formDataIn.get("name");
    const password = formDataIn.get("password");
    console.log({ name, password });

    fetch("http://localhost:8000/api/v1/login", {
      method: "POST",
      credentials: "include",
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
          alert(`HTTP error status : ${response.status}`);
          throw new Error(`HTTP error status : ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        location.replace("dashboard.html");
        console.log(`response : ${data}`);
        loginForm.reset();
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
          alert(`HTTP error status : ${response.status}`);
          throw new Error(`HTTP error status : ${response.status}`);
        }
        signupForm.reset();
        return response.json();
      })
      .then((data) => {
        console.log(`account created for ${data}, please login`);
      })
      .catch((err) => console.error(err));
  });
}

// logout functionality

if (logoutBtn) {
  logoutBtn.addEventListener("click", () => {
    fetch("http://localhost:8000/api/v1/logout", {
      method: "POST",
      credentials: "include",
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP ERROR: status ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        location.replace("/index.html");
      })
      .catch((err) => console.error(err));
  });
}

const isAuthenticated = async () => {
  const currentLocation = location.href;

  if (!currentLocation.includes("index.html")) {
    try {
      const response = await fetch("http://localhost:8000/api/v1/show", {
        credentials: "include",
      });
      if (!response.ok) {
        console.log("response not ok, redirecting");
        window.location.href = "/index.html";
        throw new Error(`HTTP erro ${response.status}`);
      }
    } catch (err) {
      console.error(`Error occured in token checking ${err}`);
    }
  }
};

isAuthenticated();
