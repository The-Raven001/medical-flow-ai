import { useState } from "react"

export function SearchPatient () {

    const [patientName, setPatientName] = useState("")
    const [patientLastName, setPatientLastName] = useState("")
    const [dateOfBirth, setDateOfBirth] = useState("")
    const [chart, setChart] = useState("")
    const [phoneNumber, setPhoneNumbser] = useState("")
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState<string | null>(null)

    //Missing portions of logic for handlesubmit

    const handlesubmit = async (event: React.SubmitEvent<HTMLFormElement>) =>{
        event.preventDefault
        setLoading(true)
        setError(null)
        
        try {
            const response = await fetch(`${process.env.NEXT_PUBLIV_API_URL}/patients`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    name: patientName,
                    lastName: patientLastName,
                    dateOfBirth: dateOfBirth,
                    chart: chart,
                    phoneNumber: phoneNumber
                })
            })

            if (!response.ok) {
                throw new Error("Failed to search patient")
            }

            const data = await response.json()
            console.log(data)

        } catch (err) {
            setError("Error occurred while searching for patient")
        } finally {
            setLoading(false)
        }
    }
    return(
        <div className="flex flex-col items-center">
            <h1>Search patient by criteria</h1>

            <form 
            className="flex flex-col mt-20 gap-4"
            onSubmit={handlesubmit} 
            >
                <input 
                className="border p-2 rounded"
                type="text"
                placeholder="Patient name"
                value={patientName}
                onChange={(event) => setPatientName(event.target.value)}
                />

                <input 
                className="border p-2 rounded"
                type="text"
                value={patientLastName}
                onChange={(event) => setPatientLastName(event.target.value)}
                 />

                <input 
                className="border p-2 rounded"
                type="date"
                value={dateOfBirth}
                onChange={(event) => setDateOfBirth(event.target.value)}
                />

                <input 
                className="border p-2 rounded"
                type="number"
                value={chart}
                onChange={(event) => setChart(event.target.value)}
                />

                <input 
                className="border p-2 rounded"
                type="text"
                value={phoneNumber}
                onChange={(event) => setPhoneNumbser(event.target.value)}
                />
            </form>
        </div>
    )
}