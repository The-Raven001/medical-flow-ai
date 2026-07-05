import { useState } from "react"

interface RegisterPayload {
    username: string
    first_name: string
    last_name: string
    email: string
    password: string
}

export function Register() {

    const [username, setUsername] = useState("")
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(false)

    const handlesubmit = async (event: React.SubmitEvent<HTMLFormElement>) => {
        event.preventDefault()
        setLoading(true)
        setError(null)

        const payload: RegisterPayload = {
            username,
            first_name: firstName,
            last_name: lastName,
            email,
            password,
        }

        try{
            const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/clinic_users`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload)
            })
            
            if (!response.ok) {
                throw new Error("Failed to register")
            }

        }
        catch (err){
            setError("Registration failed");
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="flex flex-col items-center mt-20">
            <h1 className="text-2xl mb-6">User register</h1>

            <form 
            className="flex flex-col gap-4 w-80"
            onSubmit={handlesubmit}>

                <input type="text"
                className="border p-2 rounded"
                placeholder="username"
                value={username}
                onChange={(event) => setUsername(event.target.value)}
                
                required />

                <input type="text"
                className="border p-2 rounded"
                placeholder="first name"
                value={firstName}
                onChange={(event) => setFirstName(event.target.value)}
                required />

                <input type="text"
                placeholder="last name"
                className="border p-2 rounded"
                value={lastName}
                onChange={(event) => setLastName(event.target.value)}
                required
                />

                <input 
                className="border p-2 rounded"
                type="email"
                placeholder="email"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                required />

                <input type="password"
                className="border p-2 rounded"
                placeholder="password"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                required />
                
                <button type="submit"
                className="border p-2 rounded"
                >Register</button>
            </form>
            <p>Already have an account?</p>
        </div>
    )
}