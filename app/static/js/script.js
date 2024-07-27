
function validateName(){
    const nameInput = document.getElementById('nama');
    const nameValue = nameInput.value.trim();
    
    if (nameValue === ''){
        alert('Masukan Nama Lengkap');
        nameInput.value = '';
    }
}

function validateSemester(){
    const semesterInput = document.getElementById('semester');
    const semesterValue = semesterInput.value

    if (isNaN(parseInt(semesterValue)) || semesterValue < 1 || semesterValue > 8) {
        alert('Semester harus diantara 1 dan 8');
        semesterInput.value = '';
    }
};

function validateNIM(){
    const nim = document.getElementById('nim');
    const nimValue = nim.value
    const nimLength = nimValue.length

    if (isNaN(parseInt(nimValue)) || nimLength !== 8) {
        alert('Panjang NIM harus 8 karakter');
        nim.value = '';
    }
};

function validateSubmit() {
    const nameInput = document.getElementById('nama');
    const nameValue = nameInput.value.trim();
    const nimInput = document.getElementById('nim');
    const nimValue = nimInput.value.trim();
    const fakultasSelect = document.getElementById('fakultas');
    const fakultasValue = fakultasSelect.value;
    const programStudiSelect = document.getElementById('program_studi');
    const programStudiValue = programStudiSelect.value;
    const semesterInput = document.getElementById('semester');
    const semesterValue = semesterInput.value.trim();
    
    if (nameValue === '' || nimValue === '' || fakultasValue === '' || programStudiValue === '' || semesterValue === '') {
        alert('Semua kolom harus diisi');
        return false;
    }
    return true;
}


function updateProgramStudi(){
    const fakultasSelect = document.getElementById('fakultas');
    const programStudiSelect = document.getElementById('program_studi');

    const selectedFakultasIndex = fakultasSelect.selectedIndex;

    programStudiSelect.innerHTML = '';
    console.log(selectedFakultasIndex)
    if (selectedFakultasIndex > 0) {
        console.log(programStudiOptions[selectedFakultasIndex - 1])
        const options = programStudiOptions[selectedFakultasIndex - 1];
        options.forEach((option) =>  {
            const opt = document.createElement('option');
            opt.value = option;
            opt.textContent = option;
            programStudiSelect.appendChild(opt);
        });
    }
}

function validateListForm() {
    var pilihanChecked = document.querySelectorAll('input[name="matkul_pilihan"]:checked').length;
    const pilihan = document.getElementsByName('matkul_pilihan');
    
    if (pilihan.length !== 0) {
        if (pilihanChecked === 0) {
            alert("Pilih minimal 1 mata kuliah pilihan");
            return false;
        }
    } else {
        return true;
    }
}