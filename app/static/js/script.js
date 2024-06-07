// Home
document.addEventListener("DOMContentLoaded", () => {
    const popup = document.getElementById("popup");
    const closeBtn = document.querySelector(".popup .close");
    const getStartedBtn = document.getElementById("get-started");
    const loginBtn = document.getElementById("login");
    const popupGetStartedBtn = document.getElementById("popup-get-started");

    function showPopup() {
        popup.style.display = "block";
    }

    function hidePopup() {
        popup.style.display = "none";
    }

    getStartedBtn.addEventListener("click", showPopup);
    loginBtn.addEventListener("click", showPopup);
    popupGetStartedBtn.addEventListener("click", showPopup);
    closeBtn.addEventListener("click", hidePopup);

    window.addEventListener("click", (event) => {
        if (event.target === popup) {
            hidePopup();
        }
    });
});

// Profile
document.addEventListener("DOMContentLoaded", () => {
    const editProfileButton = document.querySelector(".edit-profile-button");
    const editProfilePopup = document.querySelector("#edit-profile-popup");
    const closeBtn = document.querySelector("#edit-profile-popup .close");

    function showPopup() {
        editProfilePopup.style.display = "block";
        console.log(editProfilePopup.style.display);
    }

    function hidePopup() {
        editProfilePopup.style.display = "none";
    }

    editProfileButton.addEventListener("click", showPopup);
    closeBtn.addEventListener("click", hidePopup);

    window.addEventListener("click", (event) => {
        if (event.target === editProfilePopup) {
            hidePopup();
        }
    });
});

