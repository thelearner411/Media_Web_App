function loadDefaults(){
    let footerYear = document.getElementById("footer-year");
    let startYear = 2022;
    let date = new Date();
    let currentYear = date.getFullYear();
    footerYear.innerHTML = "© " + startYear + " - " + currentYear + " Torre Media. All Rights Reserved.";
}