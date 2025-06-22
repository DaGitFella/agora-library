import {FlashMessage} from "./FlashMessages";
import {RegisterForm, ApiResponse} from "./types";

const form = document.getElementById('profileForm') as HTMLFormElement;
const delete_btn = document.querySelector("#deleteBtn") as HTMLButtonElement;
const flash = new FlashMessage('flash-messages');
const submitBtn = document.querySelector("#submitBtn") as HTMLButtonElement;

const initialData: RegisterForm = {
    username: (form.elements.namedItem('username') as HTMLInputElement)?.value.trim(),
    email: (form.elements.namedItem('email') as HTMLInputElement)?.value.trim(),
    password: (form.elements.namedItem('password') as HTMLInputElement)?.value.trim(),
}

async function handleDelete() {
    try {
        const response = await fetch('/api/users/me', {
            method: 'DELETE',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({})
        });

        const result = await response.json();

        if (result.success && response.ok) {
            window.location.href = "/";
        } else {
            flash.show(result.message || 'Erro ao deletar usuário', 'error');
        }
    } catch {
        flash.show('erro inesperado', 'error');
    }
}

async function handleUpdate() {
    const formData: RegisterForm = {
        username: (form.elements.namedItem('username') as HTMLInputElement)?.value.trim() || '',
        email: (form.elements.namedItem('email') as HTMLInputElement)?.value.trim() || '',
        password: (form.elements.namedItem('password') as HTMLInputElement)?.value.trim() || '',
    }

    try {
        const response = await fetch('/api/users/me', {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(formData)
        })

        const result = await response.json();

        if (result.success && response.ok) {
            flash.show(result.message || 'Atualizado com sucesso', 'success');
        } else {
            flash.show(result.error || 'Erro inesperado', 'error');
        }
    } catch (e) {
        flash.show('erro inesperado', 'error');
    }
}

function checkChanges() {
    const currentData: RegisterForm = {
        username: (form.elements.namedItem('username') as HTMLInputElement)?.value.trim() || "",
        email: (form.elements.namedItem('email') as HTMLInputElement)?.value.trim() || "",
        password: (form.elements.namedItem('password') as HTMLInputElement)?.value.trim() || "",
    };


    const changed =
        currentData.username !== initialData.username ||
        currentData.email !== initialData.email ||
        currentData.password !== initialData.password;

    submitBtn.disabled = !changed;
}

delete_btn?.addEventListener('click', () => {
    handleDelete();
})

form.addEventListener('submit', (e) => {
    e.preventDefault();
    handleUpdate();
})

form.addEventListener('input', checkChanges);