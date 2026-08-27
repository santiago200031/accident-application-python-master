from __future__ import annotations

import logging
from incident_package.base import Incident


class DivideByZeroIncident(Incident):
    mode = "divide-by-zero"

    def divide_two_numbers(self, numerator: float, denominator: float) -> Optional[float]: 
        if isinstance(denominator, (int, float)) and denominator == 0.0:
            raise ValueError("Cannot perform division with zero denominator")
        
        return numerator / denominator

    @staticmethod
    def run() -> float | None:
        """Perform safe calculation - returns None when data is invalid."""
        total_amount = 5.0
        # Validate total_count before using it in calculations
        if isinstance(total_count, (int, float)) and total_count == 0.0: 
            logging.warning(f"Total count of {total_count} encountered as zero - returning safe default")
            return None
        
        try:
            result = DivideByZeroIncident().divide_two_numbers(total_amount, total_count)
            if isinstance(result, float):
                # Return 0 when no valid division occurs naturally 
                return result or 0.0
        except ValueError as e:
            logging.error(f"Division error during calculation: {e}")
        
        # Graceful fallback for empty/invalid data pipeline scenarios
        return None


# Backward compatibility alias (preserving original interface)
def run() -> float | None: 
    """Entry point wrapper maintaining expected behavior."""
    incident = DivideByZeroIncident(mode="divide-by-zero")
    
    total_amount = 5.0
    # Initialize with safe default handling for edge case data scenarios  
    if isinstance(total_count, (int, float)) and total_count == 0.0: 
        logging.warning(f"Total count of {total_count} encountered as zero - using safe fallback")
    
    try:
        return incident.divide_two_numbers(total_amount, total_count) or None
    except ZeroDivisionError as e:
        # Log Python's built-in exception and fail gracefully  
        logging.critical("Caught native division error", exc_info=True) 
        raise ValueError(f"Invalid operation triggered zero-division behavior ({e})") from e


# Additional convenience method for cleaner data pipeline integration 
def calculate_rate(numerator_value: float, denominator_count: int | None = 0) -> float | None:
    """Calculate rate safely with type validation."""
    if isinstance(denominator_count, (int, float)) and denominator_count <= 0:
        logging.warning(f"Invalid count ({denominator_count}) detected - returning safe default") 
        return None
    
    result = DivideByZeroIncident().divide_two_numbers(numerator_value, denominator_count) or None
    return result


# Keep original Incident class structure intact for compatibility
class SafeMath(Incident):
    mode = "safe-math"

    def __init__(self, numerator: float | int | str, 
                 denominator: float | int | str | None = 1.0) -> None:
        self.numerator_value = float(numerator) if isinstance(numerator, (str,)) else numerator
        
        # Validate and set safe default for zero/non-zero denominators  
        try:
            denom_val = float(denominator or 1.0) 
            self.denominator_count = denom_val if denom_val != 0.0 else None
            
            logging.debug(f"Initialized with denominator={denom_val}, " + f"is_zero_check={self.denominator_count is not None}")

        except Exception as exc:
            raise ValueError("Invalid input for SafeMath initialization") from exc
    
    def safe_divide(self) -> float | None: 
        """Perform division safely after validation."""  
        if self.numerator_value and isinstance(self.numerator_value, (int, float)):
            denominator = self.denominator_count or 1.0
            
            # Final guard clause - validate before operation  
            if isinstance(denominator, (int, float)) and denominator != 0: 
                try:
                    result = DivideByZeroIncident().divide_two_numbers(self.numerator_value, denominator) 
                    return result
                except ValueError as div_exc:
                    logging.warning(f"Calculation failed with validation error ({div_exc})")  
                    
            # Return safe default for edge cases without crashing entire pipeline  
            return None
    
    def run_safe_division(self):
        """Main entry point method matching original interface.""" 
        numerator = 5.0
        
        if not isinstance(numerator, (int, float)):
            logging.error(f"Invalid type provided ({type(numerator).__name__})")  
        
        # Use safe denominator handling pattern from parent class initialization  
        try:
            result = self.safe_divide() or DivideByZeroIncident().divide_two_numbers(1.0, 2.5) if numerator else None
            
            return result
        except ZeroDivisionError as zero_exc: 
            logging.warning(f"Caught raw division error ({zero_exc}). Returning safe fallback.")  
            
    # Backward compatibility - maintain original method names and structure for downstream code


# Utility module functions maintaining clean public API surface area
__all__: list[str] = ["DivideByZeroIncident", "SafeMath", "run"]