
import {useState} from "react"

interface LoginPayload {
    username: string
    password: string
}

export function Login() {

    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState<string | null>(null)

    const handlesubmit = async(event: React.SubmitEvent<HTMLFormElement>) => {
        event.preventDefault()
        setLoading(true)
        setError(null)

        const payload: LoginPayload = {
            username,
            password
        }

        try{
            const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload)
            })

            if(!response.ok){
                throw new Error("Failed to login")
            }
        }catch (err){
            setError("Login failed");
        } finally {
            setLoading(false)
        }
    } 

    return(
        <div className="flex flex-col items-center mt-20">
            <h1 className="text-2xl mb-6">Login</h1>
            <form 
            className="flex flex-col gap-4 w-80"
            onSubmit={handlesubmit}>

                <input type="text"
                 className="border p-2 rounded"
                 placeholder="username"
                 value={username}
                 onChange={(event) => setUsername(event.target.value)}
                 required/>

                 <input type="text" 
                 className="border p-2 rounded"
                 placeholder="password"
                 value={password}
                 onChange={(event) => setPassword(event.target.value)}
                 />

                 <button type="submit"
                 className="border p-2 rounded">
                    Enter
                 </button>

            </form>
        </div>
    )
}