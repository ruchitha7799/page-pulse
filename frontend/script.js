console.log("Page Pulse JavaScript loaded");
const API_URL = "https://page-pulse-wbkb.onrender.com/api/v1/audit";
const auditForm = document.getElementById("audit-form");
const urlInput = document.getElementById("url-input");
const auditButton = document.getElementById("audit-button");

const buttonText = document.getElementById("button-text");
const buttonLoader = document.getElementById("button-loader");

const loadingState = document.getElementById("loading-state");
const resultsContainer = document.getElementById("results-container");

const errorContainer = document.getElementById("error-container");
const errorMessage = document.getElementById("error-message");

const httpStatus = document.getElementById("http-status");
const responseTime = document.getElementById("response-time");
const h1Count = document.getElementById("h1-count");
const missingAlt = document.getElementById("missing-alt");

const pageUrl = document.getElementById("page-url");
const pageTitle = document.getElementById("page-title");
const metaDescription = document.getElementById("meta-description");
const wordCount = document.getElementById("word-count");

const statusBadge = document.getElementById("status-badge");


auditForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    console.log("Audit button clicked");
    const url = urlInput.value.trim();

    if (!url) {
        showError("Please enter a URL to audit.");
        return;
    }

    hideError();
    hideResults();
    showLoading();

    try {
        const response = await fetch(API_URL, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                url: url
            })
        });

        const result = await response.json();

        if (!response.ok || !result.success) {
            const message =
                result?.error?.message ||
                "Unable to audit this webpage.";

            throw new Error(message);
        }

        displayResults(result.data);

    } catch (error) {

        console.error(
            "Page Pulse audit error:",
            error
        );

        showError(
            error.message ||
            "Something went wrong while auditing the webpage."
        );

    } finally {

        hideLoading();

    }
});


function displayResults(data) {

    httpStatus.textContent =
        data.http_status ?? "—";

    responseTime.textContent =
        data.response_time_ms !== undefined
            ? `${data.response_time_ms} ms`
            : "—";

    h1Count.textContent =
        data.h1_count ?? "—";

    missingAlt.textContent =
        data.images_missing_alt ?? "—";


    pageUrl.textContent =
        data.url || "—";

    if (data.url) {

        pageUrl.href = data.url;

    } else {

        pageUrl.removeAttribute("href");

    }


    pageTitle.textContent =
        data.page_title ||
        "No title found";


    metaDescription.textContent =
        data.meta_description ||
        "No meta description found";


    wordCount.textContent =
        data.word_count ?? "—";


    const status =
        Number(data.http_status);


    if (
        status >= 200 &&
        status < 300
    ) {

        statusBadge.textContent =
            "Healthy";

    } else if (
        status >= 300 &&
        status < 400
    ) {

        statusBadge.textContent =
            "Redirect";

    } else {

        statusBadge.textContent =
            "Needs Attention";

    }


    resultsContainer.classList.remove(
        "hidden"
    );

    resultsContainer.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });

}


function showLoading() {

    loadingState.classList.remove(
        "hidden"
    );

    auditButton.disabled = true;

    buttonText.classList.add(
        "hidden"
    );

    buttonLoader.classList.remove(
        "hidden"
    );

}


function hideLoading() {

    loadingState.classList.add(
        "hidden"
    );

    auditButton.disabled = false;

    buttonText.classList.remove(
        "hidden"
    );

    buttonLoader.classList.add(
        "hidden"
    );

}


function showError(message) {

    errorMessage.textContent =
        message;

    errorContainer.classList.remove(
        "hidden"
    );

}


function hideError() {

    errorContainer.classList.add(
        "hidden"
    );

}


function hideResults() {

    resultsContainer.classList.add(
        "hidden"
    );

}