import { useState } from "react"

interface IntakePayload {
    first_name: string,
    last_name: string,
    date_of_birth: string,
    email: string,
    phone_number: string
}


export function Intake() {

    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [dateOfBirth, setDateOfBirth] = useState("")
    const [email, setEmail] = useState("")
    const [phoneNumber, setPhoneNumber] = useState("")

    const [loading, setLoading] = useState(false)
    const [error, setError] = useState<string | null>(null)

    const handlesubmit = async(event: React.SubmitEvent<HTMLFormElement>) => {
        event.preventDefault()
        setLoading(true)
        setError(null)

        const payload: IntakePayload = {
            first_name: firstName,
            last_name: lastName,
            date_of_birth: dateOfBirth,
            email,
            phone_number: phoneNumber
        }
        try{
            const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/intake`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })

            if(!response.ok){
                throw new Error("Intake failed")
            }

        } catch(err){
            setError("Intake form failed")
        }
    }

    

    return(
        <div className="flex flex-col items-center mt-20">
            <h1 className="text-2xl mb-6">Intake form</h1>
            <form 
            className="flex flex-col gap-4 w-80"
            onSubmit={handlesubmit}>
                <input type="text"
                className="border p-2 rounded"
                placeholder="first name"
                value={firstName}
                onChange={(event) => setFirstName(event.target.value)} />

                <input type="text"
                className="border p-2 rounded"
                placeholder="last name"
                value={lastName}
                onChange={(event) => setLastName(event.target.value)} />

                <input type="date"
                className="border p-2 rounded"
                 value={dateOfBirth}
                 onChange={(event) => setDateOfBirth(event.target.value)}/>

                 <input type="email"
                 className="border p-2 rounded"
                 placeholder="email"
                 value={email}
                 onChange={(event) => setEmail(event.target.value)} />

                 <input type="text"
                 className="border p-2 rounded"
                 placeholder="phone number"
                 value={phoneNumber}
                 onChange={(event) => setPhoneNumber(event.target.value)} />
                
                <button className="border p-2 rounded" type="submit">Send</button>
            </form>
        </div>
    )
}