import { useState } from "react"

export function SearchPatient () {

    const [patientName, setPatientName] = useState("")
    const [patientLastName, setPatientLastName] = useState("")
    const [dateOfBirth, setDateOfBirth] = useState("")
    const [chart, setChart] = useState("")
    const [phoneNumber, setPhoneNumbser] = useState("")

    //Missing logic to handlesubmit

    return(
        <div className="flex flex-col items-center items-center">
            <h1>Search patient by criteria</h1>

            <form className="flex flex-col mt-20 gap-4">
                <input 
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