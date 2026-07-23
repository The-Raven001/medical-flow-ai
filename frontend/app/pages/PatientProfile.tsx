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
    const [emergencyContactName, setEmegerncyContactName] = useState("")
    const [emergencyContactPhoneNumber, setEmergencyContactPhoneNumber] = useState("")
    const [insuranceProvider, setInsuranceProvider] = useState("")
    const [insuranceId, setInsuranceId] = useState("")
 

    return(
        <div className="flex flex-col items-center">
            <h1>Patient profile</h1>
            <div>
                <p>{firstName}</p>
                <p>{lastName}</p>
                <p>{dateOfBirth}</p>
                <p>{gender}</p>
                <p>{phoneNumber}</p>
                <p>{address}</p>
                <p>{preferredLanguage}</p>
                <p>{intakeStatus}</p>
                <p>{emergencyContactName}</p>
                <p>{emergencyContactPhoneNumber}</p>
                <p>{insuranceProvider}</p>
                <p>{insuranceId}</p>
            </div>
        </div>
    )
}