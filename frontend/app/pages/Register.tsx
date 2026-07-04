
export function Register() {

    return (
        <div className="flex flex-col items-center mt-20">
            <h1 className="text-2xl mb-6">User register</h1>

            <form 
            className="flex flex-col gap-4 w-80">

                <input type="text"
                placeholder="username"
                className="border p-2 rounded"
                required />

                <input type="text"
                placeholder="first name"
                className="border p-2 rounded"
                required />

                <input type="text"
                placeholder="last name"
                className="border p-2 rounded"
                required
                />

                <input 
                type="email"
                placeholder="email"
                className="border p-2 rounded"
                required />

                <input type="password"
                placeholder="password"
                className="border p-2 rounded"
                required />
                
                <button type="submit"
                ></button>
            </form>
            <p>Already have an account?</p>
        </div>
    )
}