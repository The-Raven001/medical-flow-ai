
import {useState} from "react"
import { set } from "zod"

interface passwordPayload {
    password: string
    newPassword: string
}

//Missing handlesubmit function as well as logic to compare passwords

export function ChangePassword() {

    const [password, setPassword] = useState("")
    const [newPassword, setNewPassword] = useState("")
    const [newReEnteredPassword, setNewReEnteredPassword] = useState("")

    return(
        <div className="">
            <h1>Update password</h1>

            <form>
                <input type="text"
                 placeholder="Enter current password" 
                 value={password}
                 onChange={(event) => setPassword(event.target.value)}
                 />

                 <input type="text"
                 placeholder="Enter new password"
                 value={newPassword}
                 onChange={(event) => setNewPassword(event.target.value)}
                  />

                  <input type="text" 
                  placeholder="Re-enter new password"
                  value={newReEnteredPassword}
                  onChange={(event) => setNewReEnteredPassword(event.target.value)}
                  />
                <button type="submit" className="border p-2 rounded">Update password</button>
            </form>
        </div>
    )
}