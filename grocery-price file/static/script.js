function fetchPrices() {
    let product = document.getElementById("product").value;
    let area = document.getElementById("area").value;

    fetch(`/get_prices?product=${product}&area=${area}`)
        .then(response => response.json())
        .then(data => {
            let output = "<h3>Price Comparison:</h3><ul>";
            if (data.length === 0) {
                output += "<li>No data found.</li>";
            } else {
                data.forEach(item => {
                    output += `<li>${item.store}: ₹${item.price}</li>`;
                });
            }
            output += "</ul>";
            document.getElementById("results").innerHTML = output;
        });
}
