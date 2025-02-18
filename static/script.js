function filterPlayers() {
    let nameInput = document.getElementById("searchBar").value.toLowerCase();
    let positionFilter = document.getElementById("positionFilter").value;
    let roleFilter = document.getElementById("roleFilter").value;
    let countryFilter = document.getElementById("countryFilter").value;
    let table = document.getElementById("playersTable");
    let divs = table.getElementsByTagName("div");

    for (let div of divs) {
        let playerName = div.getAttribute("data-name").toLowerCase();
        let playerPosition = div.getAttribute("data-position");
        let playerRole = div.getAttribute("data-role");
        let playerCountry = div.getAttribute("data-country");
        let td = div.parentElement;

        let nameMatch = playerName.includes(nameInput);
        let positionMatch = (positionFilter === "all" || playerPosition === positionFilter);
        let roleMatch = (roleFilter === "all" || playerRole === roleFilter);
        let countryMatch = (countryFilter === "all" || playerCountry === countryFilter);

        if (nameMatch && positionMatch && roleMatch && countryMatch) {
            td.style.display = "table-cell";
        } else {
            td.style.display = "none";
        }
    }
}

document.addEventListener("DOMContentLoaded", function () {
    function populateFilter(id, attribute) {
        const select = document.getElementById(id);
        const players = document.querySelectorAll("#playersTable div");
        const values = new Set(["all"]);

        players.forEach(player => values.add(player.getAttribute(attribute)));

        values.forEach(value => {
            const option = document.createElement("option");
            option.value = value;
            option.textContent = value;
            select.appendChild(option);
        });

        select.addEventListener("change", filterPlayers);
    }

    populateFilter("positionFilter", "data-position");
    populateFilter("roleFilter", "data-role");
    populateFilter("countryFilter", "data-country");
    document.getElementById("searchBar").addEventListener("keyup", filterPlayers);
});