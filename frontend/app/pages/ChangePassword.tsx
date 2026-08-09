
import {useState} from "react"

interface passwordPayload {
    password: string
    newPassword: string
}

//Missing handlesubmit function as well as logic to compare passwords

export function ChangePassword() {

    const [password, setPassword] = useState("")
    const [newPassword, setNewPassword] = useState("")
    const [newReEnteredPassword, setNewReEnteredPassword] = useState("")

    const [error, setError]= useState<string | null>(null)
    const [loading, setLoading] = useState(false)

    const payload: passwordPayload = {
    password: password,
    newPassword: newPassword
    }

    const handlesubmit = async (event: React.SubmitEvent<HTMLFormElement>) =>{
        event.preventDefault()
        setLoading(true)
        setError(null)
        //Missing logic to compare newPassword and newReEnteredPassword

        try {
            const response = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/auth/change-password`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })
        } catch (error) {
            setError("An error occurred while updating the password.")
        } finally {
            setLoading(false)
        }
    }

    return(
        <div className="flex flex-col items-center items-center">
            <h1>Update password</h1>

            <form onSubmit={handlesubmit}>
                <input type="text"
                 className="border p-2 rounded"
                 placeholder="Enter current password" 
                 value={password}
                 onChange={(event) => setPassword(event.target.value)}
                 />

                 <input type="text"
                 className="border p-2 rounded"
                 placeholder="Enter new password"
                 value={newPassword}
                 onChange={(event) => setNewPassword(event.target.value)}
                  />

                  <input type="text" 
                  className="border p-2 rounded"
                  placeholder="Re-enter new password"
                  value={newReEnteredPassword}
                  onChange={(event) => setNewReEnteredPassword(event.target.value)}
                  />
                <button type="submit" className="border p-2 rounded">Update password</button>
            </form>
        </div>
    )
}