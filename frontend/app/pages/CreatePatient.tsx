import { useState } from "react"

export function CreatePatient() {

    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [dateOfBirth, setDateOfBirth] = useState("")
    const [gender, setGender] = useState("")
    const [phoneNumber, setPhoneNumber] = useState("")
    const [email, setEmail] = useState("")
    const [address, setAddress] = useState("")
    const [preferredLanguage, setPreferredLanguage] = useState("")
    const [intakeStatus, setIntakeStatus] = useState("Not taken")
    const [emergencyContactName, setEmergencyContactName] = useState("")
    const [emergencyContactPhoneNumber, setEmergencyContactPhoneNumber] = useState("")
    const [insuraceProvider, setInsuranceProvider] = useState("")
    const [insuranceId, setInsuranceId] = useState("")
    const [providerId, setProviderId] = useState("")


    return (
        <div className="flex flex-col items-center items-center">
            <h1>Register patient</h1>
            <form className="flex flex-col mt-20 gap-4">
                <input type="text"
                className="border p-2 rounded"
                placeholder="first name"
                value={firstName}
                onChange={(event) => setFirstName(event.target.value)}
                required/>

                <input type="text"
                className=" border p-2 rounded"
                placeholder="last name"
                value={lastName}
                onChange={(event) => setLastName(event.target.value)}
                required />

                <input type="date"
                className="border p-2 rounded"
                value={dateOfBirth}
                onChange={(event) => setDateOfBirth(event.target.value)}
                required
                />

                <input type="text"
                className="border p-2 rounded"
                placeholder="gender"
                value={gender}
                onChange={(event) => setGender(event.target.value)}
                required />

                <input type="text"
                className="border p-2 rounded"
                placeholder="phone number"
                value={phoneNumber}
                onChange={(event) => setPhoneNumber(event.target.value)}
                required />

                <input type="text"
                className=""
                placeholder=""
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                required/>

                <input type="text"
                className="border p-2 rounded"
                placeholder="address"
                value={address}
                onChange={(event) => setAddress(event.target.value)}
                required />

                <input type="text"
                className="border p-2 rounded"
                placeholder="preferred language" 
                value={preferredLanguage}
                onChange={(event) => setPreferredLanguage(event.target.value)}
                required/>

                <input type="text" 
                className="border p-2 rounded"
                placeholder="intake status"
                value={intakeStatus}
                onChange={(event) => setIntakeStatus(event.target.value)}
                required/>

                <input type="text" 
                className="border p-2 rounded"
                placeholder="emergency contact name"
                value={emergencyContactName}
                onChange={(event) => setEmergencyContactName(event.target.value)}
                />

                <input type="text" 
                className="border p-2 rounded"
                placeholder="emergency contact phone number"
                value={emergencyContactPhoneNumber}
                onChange={(event) => setEmergencyContactPhoneNumber(event.target.value)}
                />

                <input type="text"
                className="border p-2 rounded"
                placeholder="insurance provider"
                value={insuraceProvider}
                onChange={(event) => setInsuranceProvider(event.target.value)}
                required
                />

                <input type="text"
                className="border p-2 rounded"
                placeholder="insurance id"
                value={insuranceId}
                onChange={(event) => setInsuranceId(event.target.value)}
                required />

                <input type="number"
                className="border p-2 rounded" 
                placeholder="provider id"
                value={providerId}
                onChange={(event) => setProviderId(event.target.value)}
                required />
            </form>
        </div>
    )
}