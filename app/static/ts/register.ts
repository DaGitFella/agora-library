import {RegisterForm, ApiResponse} from "./types";
import {FlashMessage} from "./FlashMessages";

const form = document.querySelector("#registerForm") as HTMLFormElement;
const flash = new FlashMessage('flash-messages');

async function submitForm() {
    const formData: RegisterForm = {
        username: (form.elements.namedItem('username') as HTMLInputElement).value.trim(),
        email: (form.elements.namedItem('email') as HTMLInputElement).value.trim(),
        password: (form.elements.namedItem('password') as HTMLInputElement).value.trim(),
    };

    try {
        const response = await fetch('api/auth/register', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(formData),
        });

        const result: ApiResponse = await response.json();

        if (response.ok && result.success) {
            flash.show(result.message || 'Registrado com sucesso', 'success');
            form.reset();
        } else {
            flash.show(result.error || 'Erro inesperado', 'error');
        }
    } catch {
        flash.show('Erro de conexão', 'error');
    }
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    submitForm();
})