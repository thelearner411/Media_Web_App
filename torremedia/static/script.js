function loadDefaults(){
    let footerYear = document.getElementById("footer-year");
    let date = new Date();
    let currentYear = date.getFullYear();
    footerYear.innerHTML = "© " + currentYear + " Torre Media. All Rights Reserved.";
}