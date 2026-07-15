import { useState } from "react"

interface UpdatePayload {
    first_name: string
    last_name: string
    date_of_birth: string
    gender: string
    phone_number: string
    email: string
    address: string
    preferred_language: string
    intake_status: string
    emergency_contact_name: string
    emergency_contact_phone_number: string
    insurance_provider: string
    insurance_id: string
    provider_id: string
}

// Function to load current patient is missing

export function EditPatient() {

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
    
    const [error, setError]= useState<string | null>(null)
    const [loading, setLoading] = useState(false)

    const payload: UpdatePayload = {
        first_name: firstName,
        last_name: lastName,
        date_of_birth: dateOfBirth,
        gender,
        phone_number: phoneNumber,
        email,
        address,
        preferred_language: preferredLanguage,
        intake_status: intakeStatus,
        emergency_contact_name: emergencyContactName,
        emergency_contact_phone_number: emergencyContactPhoneNumber,
        insurance_provider: insuraceProvider,
        insurance_id: insuranceId,
        provider_id: providerId
    }

    const handlesubmit = async (event: React.SubmitEvent<HTMLFormElement>) =>{
        event.preventDefault
        setLoading(true)
        setError(null)

        try{
            const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/patients`, {
                method: "POST",
                headers: {
                    "Content-Type": "application.json",
                },
                body: JSON.stringify(payload)
            })
            if (!response.ok){
                throw new Error("Failed to create profile of patient")
        }
        }
        catch (err){
            setError("Registration failed")
        } finally {setLoading(false)}
    }

    return (
        <div className="flex flex-col items-center items-center">
            <h1>Update patient</h1>
            <form 
            className="flex flex-col mt-20 gap-4"
            onSubmit={handlesubmit}>
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
            <button type="submit" className="border p-2 rounded">Update</button>
        </div>
    )
}