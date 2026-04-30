// adresa backend-ului (fast-api)
const API = window.location.origin;


// incarcare angajati cu get
async function loadAngajati() {
    try {
        // trimit request la backend
        const res = await fetch(`${API}/angajati`);

        // primesc lista de angajati din baza de date
        const angajati = await res.json();

        const tabel = document.getElementById("tabelAngajati");
        tabel.innerHTML = ""; // golesc tabelul

        // parcurg fiecare angajat primit
        angajati.forEach(ang => {
            tabel.innerHTML += `
                <div class="angajat">
                    <div class="infoAngajat">
                        <div class="infoAngajatImagine">
                            <img src="https://e7.pngegg.com/pngimages/1014/378/png-clipart-shetland-sheep-computer-icons-black-sheep-wool-glass-glass-logo.png"
                                alt="angajat" />
                        </div>
                        <div class="infoAngajatNume">
                            <p><strong>${ang.nume} ${ang.prenume}</strong></p>
                            <p>${ang.email}</p>
                            <p>${ang.localitate}, ${ang.judet}</p>
                            <p>${ang.rol} • ${ang.varsta} ani</p>
                        </div>
                    </div>
                    <button class="stergereAngajat" onclick="stergeAngajat(${ang.id})">Stergere</button>
                </div>`;
        });

    } catch (err) {
        arataMesaj("Nu s-au putut incarca angajatii.", "red");
    }
}


// adaugare angajati cu post
async function adaugaAngajat() {

    // iau datele din formular
    const angajat = {
        nume:       document.getElementById("nume").value,
        prenume:    document.getElementById("prenume").value,
        email:      document.getElementById("email").value,
        localitate: document.getElementById("localitate").value,
        judet:      document.getElementById("judet").value,
        rol:        document.getElementById("rol").value,
        varsta:     document.getElementById("varsta").value
    };

    // verific daca sunt completate toate campurile
    if (!angajat.nume || !angajat.prenume || !angajat.email || !angajat.localitate || !angajat.judet || !angajat.rol || !angajat.varsta) {
        arataMesaj("Completeaza toate campurile.", "orange");
        return;
    }

    try {
        // post /angajati
        const res = await fetch(`${API}/angajati`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(angajat),
        });

        const data = await res.json();

        if (res.ok) {
            arataMesaj(data.message, "green");

            // golesc formularul
            ["nume", "prenume", "email", "localitate", "judet", "rol", "varsta"].forEach(id => {
                document.getElementById(id).value = "";
            });

            // incarc din nou lista din baza de date
            loadAngajati();
        } else {
            arataMesaj(data.detail, "red");
        }

    } catch (err) {
        arataMesaj("Nu s-a putut conecta la server.", "red");
    }
}


// stergere angajat
async function stergeAngajat(id) {

    if (!confirm(`Stergi angajatul #${id}?`)) return;

    try {
        const res = await fetch(`${API}/angajati/${id}`, {
            method: "DELETE"
        });

        const data = await res.json();
        arataMesaj(data.message, res.ok ? "green" : "red");

        if (res.ok) loadAngajati();

    } catch (err) {
        arataMesaj("Eroare la stergere.", "red");
    }
}


// mesaje ui
function arataMesaj(msg, color = "black") {
    const el = document.getElementById("mesaj");
    el.textContent = msg;
    el.style.color = color;
}


// la deschiderea paginii incarc angajatii
loadAngajati();