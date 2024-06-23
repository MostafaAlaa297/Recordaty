document.addEventListener("DOMContentLoaded", () => {
    // Register popup
    const registerPopup = document.getElementById("register-popup");
    const registerCloseBtn = document.querySelector(".register-popup .register-close");
    const registerGetStartedBtn = document.getElementById("get-started");
    const registerPopupGetStartedBtn = document.getElementById("popup-get-started");

    function showRegisterPopup() {
        registerPopup.style.display = "block";
    }

    function hideRegisterPopup() {
        registerPopup.style.display = "none";
    }

    if (registerGetStartedBtn) {
        registerGetStartedBtn.addEventListener("click", showRegisterPopup);
    }

    if (registerPopupGetStartedBtn) {
        registerPopupGetStartedBtn.addEventListener("click", showRegisterPopup);
    }

    if (registerCloseBtn) {
        registerCloseBtn.addEventListener("click", hideRegisterPopup);
    }

    window.addEventListener("click", (event) => {
        if (event.target === registerPopup) {
            hideRegisterPopup();
        }
    });

    // Login Popup
    const loginPopup = document.getElementById("login-popup");
    const loginCloseBtn = document.querySelector(".login-popup .login-close");
    const loginBtn = document.getElementById("login");

    function showLoginPopup() {
        loginPopup.style.display = "block";
    }

    function hideLoginPopup() {
        loginPopup.style.display = "none";
    }

    if (loginBtn) {
        loginBtn.addEventListener("click", showLoginPopup);
    }

    if (loginCloseBtn) {
        loginCloseBtn.addEventListener("click", hideLoginPopup);
    }

    window.addEventListener("click", (event) => {
        if (event.target === loginPopup) {
            hideLoginPopup();
        }
    });

    // Add condition
    const addConditionBtn = document.querySelector(".add-condition");
    const newConditionInput = document.getElementById("new-condition-input");
    const addConditionButton = document.getElementById("add-condition-button");
    const profileConditions = document.querySelector(".profile-conditions");

    if (addConditionBtn && newConditionInput && addConditionButton && profileConditions) {
        addConditionBtn.addEventListener("click", () => {
            newConditionInput.style.display = "block";
            addConditionButton.style.display = "block";
            newConditionInput.focus();
        });

        addConditionButton.addEventListener("click", () => {
            const newCondition = newConditionInput.value.trim();
            if (newCondition) {
                const conditionDiv = document.createElement("div");
                conditionDiv.className = "condition";
                conditionDiv.textContent = newCondition;
                profileConditions.insertBefore(conditionDiv, addConditionBtn);
                attachConditionEvent(conditionDiv);
                newConditionInput.value = "";
                newConditionInput.style.display = "none";
                addConditionButton.style.display = "none";
            }
        });
    }

    // Attach event listener to existing conditions
    document.querySelectorAll(".profile-conditions .condition").forEach(attachConditionEvent);

    // Condition Info Popup
    const conditionInfoPopup = document.getElementById("condition-info-popup");
    const conditionInfoClose = document.querySelector(".condition-info-close");

    function showConditionInfoPopup() {
        conditionInfoPopup.style.display = "block";
    }

    function hideConditionInfoPopup() {
        conditionInfoPopup.style.display = "none";
    }

    if (conditionInfoClose) {
        conditionInfoClose.addEventListener("click", hideConditionInfoPopup);
    }

    window.addEventListener("click", (event) => {
        if (event.target === conditionInfoPopup) {
            hideConditionInfoPopup();
        }
    });

    function attachConditionEvent(conditionDiv) {
        conditionDiv.addEventListener("click", showConditionInfoPopup);
    }

      // Table Search
      function filterTable() {
        const input = document.getElementById("myInput");
        const filter = input.value.toUpperCase();
        const table = document.getElementById("condition-info-table");
        const tr = table.getElementsByTagName("tr");

        for (let i = 1; i < tr.length; i++) {
          let display = false;
          const tds = tr[i].getElementsByTagName("td");
          for (let j = 0; j < tds.length; j++) {
            if (tds[j]) {
              const txtValue = tds[j].textContent || tds[j].innerText;
              if (txtValue.toUpperCase().indexOf(filter) > -1) {
                display = true;
                break;
              }
            }
          }
          tr[i].style.display = display ? "" : "none";
        }
      }

      const input = document.getElementById("myInput");
      input.addEventListener("keyup", filterTable);
});
