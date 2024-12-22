document.getElementById('show-pass').addEventListener('change', function() {
    const passInput = document.getElementById('team-pass');
    if (this.checked) {
        passInput.type = 'text';
    } else {
        passInput.type = 'password';
    }
});

document.getElementById('team-form').addEventListener('submit', function(event) {
    event.preventDefault();
    addOrUpdateTeam('add');
});

document.getElementById('update-team').addEventListener('click', function() {
    addOrUpdateTeam('update');
});

let editingTeamIndex = -1;

function addOrUpdateTeam(action) {
    const name = document.getElementById('team-name').value;
    const pass = document.getElementById('team-pass').value;
    const description = document.getElementById('team-description').value;
    const logo = document.getElementById('team-logo').files[0];

    if (!logo) {
        alert('Please select a team logo');
        return;
    }

    const reader = new FileReader();
    reader.onload = function(e) {
        const logoUrl = e.target.result;
        if (action === 'add') {
            addTeam(name, pass, description, logoUrl);
        } else if (action === 'update' && editingTeamIndex !== -1) {
            updateTeam(name, pass, description, logoUrl, editingTeamIndex);
        }
    };
    reader.readAsDataURL(logo);

    clearForm();
}

function addTeam(name, pass, description, logoUrl) {
    const teamList = document.getElementById('team-list');
    const teamItem = createTeamItem(name, pass, description, logoUrl, teamList.childElementCount);
    teamList.appendChild(teamItem);
}

function updateTeam(name, pass, description, logoUrl, index) {
    const teamList = document.getElementById('team-list');
    const teamItem = createTeamItem(name, pass, description, logoUrl, index);
    teamList.replaceChild(teamItem, teamList.children[index]);
    editingTeamIndex = -1;
}
function toggleDescription(element) {
    const teamItem = element.closest('.team-item');
    const description = teamItem.querySelector('.description');
    const fullDescription = teamItem.querySelector('.full-description');

    if (fullDescription.style.display === 'none') {
        fullDescription.style.display = 'block';
        element.innerText = 'Show more';
    } else {
        fullDescription.style.display = 'none';
        element.innerText = 'Show less';
    }
}
function createTeamItem(name, pass, description, logoUrl, index) {
    const teamItem = document.createElement('div');
    teamItem.className = 'team-item';

    teamItem.innerHTML = `
        <img src="${logoUrl}" alt="Logo">
        <div class="team-info">
            <h3>${name}</h3>
            <p class="description">
                ${description.split('.')[0]}.
            </p>
            <p class="full-description">
                ${description}
            </p>
            <span class="show-more" onclick="toggleDescription(this)">Show more</span>
            <small>Password: ${pass}</small>
        </div>
        <div class="team-buttons">
            <button class="edit" onclick="editTeam(${index})">Edit</button>
            <button class="delete" onclick="deleteTeam(${index})">Delete</button>
        </div>
    `;

    return teamItem;
}
function editTeam(index) {
    const teamList = document.getElementById('team-list');
    const teamItem = teamList.children[index];
    const passwordText = teamItem.querySelector('small').innerText.split(': ')[1];

    document.getElementById('team-name').value = teamItem.querySelector('h3').innerText;
    document.getElementById('team-pass').value = passwordText; // Populate the password field correctly
    document.getElementById('team-description').value = teamItem.querySelector('.full-description').innerText.trim().replace('Show less', '');

    editingTeamIndex = index;
}

function deleteTeam(index) {
    const teamList = document.getElementById('team-list');
    teamList.removeChild(teamList.children[index]);
    editingTeamIndex = -1;
}

function toggleDescription(element) {
    const teamItem = element.closest('.team-item');
    const description = teamItem.querySelector('.description');
    const fullDescription = teamItem.querySelector('.full-description');

    if (fullDescription.style.display === 'none') {
        fullDescription.style.display = 'block';
        description.style.display = 'none'; // Hide truncated text
        element.innerText = 'Show more';
    } else {
        fullDescription.style.display = 'none';
        description.style.display = 'block'; // Show truncated text
        element.innerText = 'Show less';
    }
}

function clearForm() {
    document.getElementById('team-form').reset();
}
