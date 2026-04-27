async function initializeBureau() {
    const assetList = document.getElementById('asset-list');
    const passportData = document.getElementById('passport-data');
    const cacheBuster = "?v=" + Date.now();
    
    try {
        console.log("PADI: Initiating Sovereign Handshake...");
        const response = await fetch("./manifest.json" + cacheBuster);
        if (!response.ok) throw new Error("Manifest Offline");
        const manifest = await response.json();

        passportData.innerHTML = `
            <div class="identity-grid">
                <p><strong>Architect:</strong> ${manifest.governing_architect}</p>
                <p><strong>Status:</strong> Online & Fortified</p>
                <p><strong>Registry:</strong> ${manifest.zenodo_doi}</p>
            </div>`;

        assetList.innerHTML = manifest.assets.map(asset => 
            `<li class="asset-item">
                <strong>[${asset.type.toUpperCase()}]</strong> ${asset.name}
                <br><code style="font-size: 0.7em; color: #238636;">SHA256: ${asset.sha256.substring(0, 16)}...</code>
            </li>`).join('');

        document.getElementById('status-badge').innerText = "Status: Online & Fortified";

    } catch (error) {
        console.error("Handshake Failed:", error);
        passportData.innerHTML = `
            <p style="color: #f85149;"><strong>Handshake Offline</strong></p>
            <p style="font-size: 0.8em;">The Kernel is currently rebasing. Check back in 60s.</p>`;
    }
}
document.addEventListener('DOMContentLoaded', initializeBureau);
