import { useState } from "react"

export function PatientProfile () {

    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [dateOfBirth, setDateOfBirth] = useState("")
    const [gender, setGender] = useState("")
    const [phoneNumber, setPhoneNumber] = useState("")
    const [address, setAddress] = useState("")
    const [preferredLanguage, setPreferredLanguage] = useState("")
    const [intakeStatus, setIntakeStatus] = useState("")
    const [emergencyContactName, setEmergencyContactName] = useState("")
    const [emergencyContactPhoneNumber, setEmergencyContactPhoneNumber] = useState("")
    const [insuranceProvider, setInsuranceProvider] = useState("")
    const [insuranceId, setInsuranceId] = useState("")
 

    return(
        <div className="flex flex-col items-center">
            <h1>Patient profile</h1>
            <div className="flex flex-col mt-20 gap-4">
                <p className="border p-2 rounded">{firstName}</p>
                <p className="border p-2 rounded">{lastName}</p>
                <p className="border p-2 rounded">{dateOfBirth}</p>
                <p className="border p-2 rounded">{gender}</p>
                <p className="border p-2 rounded">{phoneNumber}</p>
                <p className="border p-2 rounded">{address}</p>
                <p className="border p-2 rounded">{preferredLanguage}</p>
                <p className="border p-2 rounded">{intakeStatus}</p>
                <p className="border p-2 rounded">{emergencyContactName}</p>
                <p className="border p-2 rounded">{emergencyContactPhoneNumber}</p>
                <p className="border p-2 rounded">{insuranceProvider}</p>
                <p className="border p-2 rounded">{insuranceId}</p>
            </div>
        </div>
    )
}