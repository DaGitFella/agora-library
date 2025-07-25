export interface RegisterForm {
    username: string
    email: string
    password: string
}

export interface LoginForm {
    email: string
    password: string
}

export interface ApiResponse {
    success: boolean
    message?: string
    error?: string
}
