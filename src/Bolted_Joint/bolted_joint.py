class BoltedJoint:
    def __init__(self, bolt_diameter, thread_pitch, bolt_material, clamped_material):
        self.bolt_diameter = bolt_diameter
        self.thread_pitch = thread_pitch
        self.bolt_material = bolt_material
        self.clamped_material = clamped_material
    
    def bolt_preload(self, torque):
        bolt_area = math.pi / 4 * self.bolt_diameter ** 2
        bolt_stress = torque / bolt_area / self.bolt_material.yield_strength
        return bolt_stress * bolt_area
    
    def bolt_tension(self, preload):
        bolt_area = math.pi / 4 * self.bolt_diameter ** 2
        bolt_stress = preload / bolt_area
        return bolt_stress * bolt_area
    
    def bolt_shear(self, applied_load):
        bolt_area = math.pi / 4 * self.bolt_diameter ** 2
        bolt_stress = applied_load / bolt_area
        return bolt_stress * bolt_area
    
    def bolt_bearing(self, applied_load):
        clamped_area = self.bolt_diameter * self.clamped_material.thickness
        clamped_stress = applied_load / clamped_area
        return clamped_stress * clamped_area
    
    def bolt_fatigue_life(self, applied_load, cycles):
        bolt_area = math.pi / 4 * self.bolt_diameter ** 2
        bolt_stress = applied_load / bolt_area
        fatigue_strength = self.bolt_material.fatigue_strength(bolt_stress)
        return fatigue_strength / applied_load * cycles
    
    def joint_stiffness(self):
        clamped_area = self.bolt_diameter * self.clamped_material.thickness
        return self.clamped_material.elastic_modulus * clamped_area / self.clamped_material.length
    
    def joint_strength(self):
        clamped_area = self.bolt_diameter * self.clamped_material.thickness
        clamped_stress = self.clamped_material.yield_strength
        return clamped_stress * clamped_area
    
    def joint_safety_factor(self, applied_load):
        return self.joint_strength() / applied_load
    
    def output_results(self, applied_load, torque, cycles):
        preload = self.bolt_preload(torque)
        tension = self.bolt_tension(preload)
        shear = self.bolt_shear(applied_load)
        bearing = self.bolt_bearing(applied_load)
        fatigue_life = self.bolt_fatigue_life(applied_load, cycles)
        stiffness = self.joint_stiffness()
        strength = self.joint_strength()
        safety_factor = self.joint_safety_factor(applied_load)
        
        print(f"Bolt preload: {preload:.2f} N")
        print(f"Bolt tension: {tension:.2f} N")
        print(f"Bolt shear: {shear:.2f} N")
        print(f"Bolt bearing: {bearing:.2f} N")
        print(f"Bolt fatigue life: {fatigue_life:.2f} cycles")
        print(f"Joint stiffness: {stiffness:.2f} N/m")
        print(f"Joint strength: {strength:.2f} N")
        print(f"Joint safety factor: {safety_factor:.2f}")
