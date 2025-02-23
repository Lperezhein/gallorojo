

document.addEventListener("DOMContentLoaded", function () {
    let breadcrumb = document.querySelector(".breadcrumb");

    if (breadcrumb) {
        console.log("Breadcrumbs cargados correctamente.");
        
        // Obtener la ruta actual y dividirla en partes
        let path = window.location.pathname.split("/").filter(p => p);
        let breadcrumbList = breadcrumb.querySelector("ol");

        if (breadcrumbList && path.length > 0) {
            breadcrumbList.innerHTML = `<li class="breadcrumb-item"><a href="/">Inicio</a></li>`;

            let url = "/";
            path.forEach((segment, index) => {
                url += segment + "/";
                let isLast = index === path.length - 1;

                breadcrumbList.innerHTML += isLast
                    ? `<li class="breadcrumb-item active" aria-current="page">${decodeURIComponent(segment)}</li>`
                    : `<li class="breadcrumb-item"><a href="${url}">${decodeURIComponent(segment)}</a></li>`;
            });
        }
    } else {
        console.error("⚠️ No se encontró la clase .breadcrumb en el HTML.");
    }
});
