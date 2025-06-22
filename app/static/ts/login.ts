import {LoginForm, ApiResponse, RegisterForm} from "./types";
import {FlashMessage} from "./FlashMessages";

const form = document.querySelector("#loginForm") as HTMLFormElement;
const flash = new FlashMessage('flash-messages');

async function submitLogin() {
    const formData: LoginForm = {
        email: (form.elements.namedItem('email') as HTMLInputElement).value.trim(),
        password: (form.elements.namedItem('password') as HTMLInputElement).value.trim(),
    };

    try {
        const response = await fetch('api/auth/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(formData),
        })

        const result = await response.json();

        if (response.ok && result.success) {
            flash.show(result.message || 'Usuário logado com sucesso!');
            form.reset();
        } else {
            flash.show(result.message || 'Erro inesperado', 'error');
        }
    } catch {
        flash.show('erro inesperado', 'error');
    }
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    submitLogin();
});